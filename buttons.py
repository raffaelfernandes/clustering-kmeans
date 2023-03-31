from abc import (ABC, abstractmethod)
import controlador_kmeans as ck
import numpy as np

class janela(ABC):
  @abstractmethod
  def criar(sg, dims):
    pass

class janela_2d(janela):
  def criar(sg, k):
    data = np.random.uniform(low=0, high=100, size=(200,2))
    centroids, clusters = ck.k_means(data, k, 2)
    ck.plot_grafico_2d(centroids, clusters, data)

    layout_2d = [[sg.Text('Plotagem do Gráfico 2D', font=('Helvetica', 12, 'bold'))],[sg.Push()],[sg.Image(filename='grph.png',)]]
    criar_janela = sg.Window('   Plotagem 2D', layout_2d, element_justification='c', size=(650,500))
    criar_janela.set_icon('')
    
    while True:
      evento, valores = criar_janela.read()
      if evento == sg.WIN_CLOSED:
        criar_janela.close()
        break
    pass

class janela_3d(janela):
  def criar(sg, k):
    layout_3d = [[sg.Text('Plotagem do Gráfico 3D', font=('Helvetica', 12, 'bold'))],[sg.Push()],[sg.Image(filename='grph.png',)]]
    criar_janela = sg.Window('   Plotagem 3D', layout_3d, element_justification='c', size=(700,500))
    criar_janela.set_icon('')
    data = np.random.uniform(low=0, high=100, size=(200,3))
    centroids, clusters = ck.k_means(data, k, 3)
    ck.plot_grafico_3d(centroids, clusters, data)

    
    while True:
      evento, valores = criar_janela.read()
      if evento == sg.WIN_CLOSED:
        criar_janela.close()
        break
    pass

class janela_maisd(janela):
      
  def criar_maisd(sg, k, dims):
    def text(centroids, k, dims):
      string = ''
      for i in range(k):
        string += f'\n\nCentróide {i+1}:\n'
        for j in range(dims):
          string += f'Cord.{j+1} = ('+'{:.2f}); '.format(centroids[i][j])
          if (j+1)%5 == 0:
            string += '\n'
      return string

    data = np.random.uniform(low=0, high=100, size=(200,dims))
    centroids, clusters = ck.k_means(data, k, dims)
    string = text(centroids, k, dims)
    
    layout = [[sg.Text(f'Coordenadas dos centróides\npara {dims} dimensões:', font=('Helvetica', 12, 'bold'))],[sg.Text(string)]]
    criar_maisd = sg.Window('   Dados para mais dimensões', layout, element_justification='c', size=(700,600))
    
    while True:
      evento, valores = criar_maisd.read()
      if evento == sg.WIN_CLOSED:
        criar_maisd.close()
        break
    pass