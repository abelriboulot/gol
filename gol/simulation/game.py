import torch
from torch.nn import functional as F
from pyinform import active_info, utils
import json
import numpy as np

create_random_p = lambda x, p: (torch.cuda.FloatTensor(x.shape).normal_().uniform_() < p).float().cuda()

def step_gol(X, p_stasis=1., p_overpopulation=0., p_underpopulation=0., p_reproduction=1.):
    """ Takes a step to adjust the world according to probabilities for each action. """
    filt = torch.ones(3, 3).long().unsqueeze_(0).unsqueeze_(0).cuda()

    # The world should follow torroidal geometry, therefore we need to wrap the space
    # this is achieved by padding in this case.
    n = X.size(-1)
    X_wrapped = X.repeat(n, n)[(n - 1):(2 * n + 1), (n - 1):(2 * n + 1)].unsqueeze_(0).unsqueeze_(0)

    mask_overpopulation = create_random_p(X, p_overpopulation)
    mask_underpopulation = create_random_p(X, p_underpopulation)
    mask_stasis = create_random_p(X, p_stasis) * X
    mask_reproduction = create_random_p(X, p_reproduction)

    dead_mask = torch.zeros(X.shape).cuda()

    X_count = F.conv2d(X_wrapped.float(), filt.float()).squeeze()

    X_new = torch.where(X_count > 3, mask_overpopulation, dead_mask) + \
            torch.where(X_count == 3, mask_reproduction, dead_mask) + \
            torch.where(X_count == 2, mask_stasis, dead_mask) + \
            torch.where(X_count == 1, mask_underpopulation, dead_mask)

    return X_new.long()

#TODO Websocket
def write_gol(X, json_outfile = '/home/paperspace/research/game_of_life/data/test.json'):
    with open(json_outfile, 'w') as outfile:
        json.dump(X.cpu().numpy().tolist(), outfile)

def game_loop(size=10, initial_p_alive=0.1, n_iters=1000,
              p_stasis=1., p_overpopulation=0., p_underpopulation=0., p_reproduction=1.):
    X = (torch.rand(size,size) < initial_p_alive).long().cuda()
    states = []
    ts_alive = []
    for i in range(n_iters):
        X = step_gol(X, p_stasis=p_stasis, p_overpopulation=p_overpopulation,
                     p_underpopulation=p_underpopulation, p_reproduction=p_reproduction)
        write_gol(X)
        encoded_state = utils.encode(X[:4,:2].reshape(-1).cpu(), b=2)
        states.append(encoded_state)
        ts_alive.append(X.sum().cpu().numpy())

    return active_info(states, k=2), np.mean(ts_alive)
