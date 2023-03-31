import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def k_means(data, k, dims, max_iters=100):
  shape = (200, dims)
  centroids = data[np.random.choice(data.shape[0], size=k, replace=False), :]  
  
  for i in range(max_iters):
      # Etapa de associação: calcular as distâncias euclidianas entre cada ponto de dados e os centroides
    distances = np.sqrt(((data - centroids[:, np.newaxis])**2).sum(axis=2))
    clusters = np.argmin(distances, axis=0)
      
      # Etapa de atualização: atualizar os centroides para a média de cada cluster
    for j in range(k):
      centroids[j] = np.mean(data[clusters == j], axis=0)
  
    return centroids, clusters

def plot_grafico_2d(centroids, clusters, data):
  fig, ax = plt.subplots()
  ax.scatter(data[:, 0], data[:, 1], c=clusters)
  ax.scatter(centroids[:, 0], centroids[:, 1], s=80, color='red', label='Centróides', alpha=0.5)
  ax.set_xlabel('Eixo X')
  ax.set_ylabel('Eixo Y')
  ax.legend(loc='lower left')
  plt.savefig('grph.png', format='png')
  imagem = Image.open('grph.png')
  larg, alt = imagem.size
  imagem = imagem.resize((int(larg/1.2), int(alt/1.2)))
  imagem.save('grph.png')

def plot_grafico_3d(centroids, clusters, data):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=clusters)
  ax.scatter(centroids[:, 0], centroids[:, 1], centroids[:, 2], s=80, color='red', label='Centróides', alpha=0.5)
  ax.set_xlabel('Eixo X')
  ax.set_ylabel('Eixo Y')
  ax.set_zlabel('Eixo Z')
  ax.legend(loc='upper left')
  fig.savefig('grph.png', format='png')
  imagem = Image.open('grph.png')
  larg, alt = imagem.size
  imagem = imagem.resize((int(larg/1.1), int(alt/1.1)))
  nova_larg, nova_alt = imagem.size
  left = int(nova_larg/7)
  top = int(nova_alt/9)
  right = nova_larg - int(nova_larg/12)
  bottom = alt
  imagem = imagem.crop((left, top, right, bottom))
  imagem.save('grph.png')
  