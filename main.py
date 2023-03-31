import PySimpleGUI as sg
import buttons

sg.theme('DarkTeal1')
# Layout
gui_layout = [[sg.Image(filename='images/Cluster.png')],[sg.Push()],[sg.Text('Clustering com K-Means', font=('Helvetica', 14, 'bold'))],[sg.Push()],[sg.Text('Selecione uma opção para o tamanho\ndas dimensões dos dados:', font=('Arial', 12, 'normal'))],\
[sg.Push()],[sg.Combo(['2', '3', '4', '5', '6', '7', '8', '9', '10'], size=(20, 1), key=('-dim-'), default_value=('Clique para selecionar'))],[sg.Push()],[sg.Text('Digite a quantidade de centróides:', font=('Arial', 12, 'normal'))],[sg.Push()],[sg.Input(key=('-cents-'), size=(5, 0))],[sg.Button('OK')]]

#janela
menu_janela = sg.Window('Clustering com K-means', gui_layout, element_justification='c', size=(500,400))
menu_janela.set_icon('')

while True:
  evento, valores = menu_janela.read()
  if evento == sg.WIN_CLOSED:
    break
  if evento == 'OK':
    if (valores['-dim-'] == 'Clique para selecionar' or int(valores['-dim-']) <  2 or valores['-cents-'] == None or valores['-cents-'] == ''):
      sg.popup('Campos Inválidos!', title='   Erro!')
    elif int(valores['-dim-']) == 2:
      buttons.janela_2d.criar(sg, int(valores['-cents-']))
    elif int(valores['-dim-']) == 3:
      buttons.janela_3d.criar(sg, int(valores['-cents-']))
    elif int(valores['-dim-']) > 3:
      buttons.janela_maisd.criar_maisd(sg, int(valores['-cents-']), int(valores['-dim-']))
menu_janela.close()