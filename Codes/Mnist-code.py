from sklearn.datasets import fetch_openml

mnist = fetch_openml('mnist_784')

x = mnist.data
y = mnist.target

print(mnist.shape())