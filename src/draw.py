from draw_neural_net import draw_neural_net
from matplotlib import pyplot as plt

size = list(map(int, input("Enter NN layers: ").split()))

fig = plt.figure()
draw_neural_net(fig.gca(), size)
plt.title("-".join([str(s) for s in size]) + " neural network")
plt.show()
