import torch

def test_step_gol():
    """ Unit test for the gol """
    test_field = torch.tensor([[0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

    # Checking that the game works properly
    assert torch.all(torch.eq(step(test_field), torch.tensor([[0, 1, 1, 1],
                                                              [0, 0, 1, 0],
                                                              [0, 0, 0, 0],
                                                              [0, 0, 1, 0]])))
    return