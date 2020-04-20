from gol import game_loop

print(game_loop(100, initial_p_alive=.1, p_stasis=1., p_overpopulation=0., p_underpopulation=0., p_reproduction=1.))