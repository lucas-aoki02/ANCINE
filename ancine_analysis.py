# Importação dos dados
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ancine = pd.read_csv('C:/LUCAS/dados/projetos_dados/ANCINE/ancine_files/BilheteriaObrasSemana.csv')

# Renomeação de colunas
ancine = ancine.rename(columns={'TITULO_BRASILEIRO':'TITULO'})
ancine = ancine.rename(columns={'PAIS_ORIGEM':'PAIS'})

#Exclusão de colunas 
ancine_mod = ancine.drop(ancine.columns[[0, 4, 5, 6, 7, 8, 11, 12, 13, 14]], axis=1)

#Verificação se há registros nulos
ancine_mod.isnull().sum()

#Descriminando os 5 países com maior oferta
pais = ancine_mod['PAIS'].value_counts()
pais.index #EUA, Brasil, França, Alemanha e Reino Unido

#Filtragem da RENDA de ACORDO c/o país 
renda_eua = ancine_mod.loc[ancine_mod['PAIS'] == ' Estados Unidos']
renda_eua = renda_eua.RENDA.sum()
renda_eua = np.log10(renda_eua)

renda_br = ancine_mod.loc[ancine_mod['PAIS'] == ' Brasil']
renda_br = renda_br.RENDA.sum()
renda_br = np.log10(renda_br)

renda_fr = ancine_mod.loc[ancine_mod['PAIS'] == ' França']
renda_fr = renda_fr.RENDA.sum()
renda_fr = np.log10(renda_fr)

renda_ger = ancine_mod.loc[ancine_mod['PAIS'] == ' Alemanha']
renda_ger = renda_ger.RENDA.sum()
renda_ger = np.log10(renda_ger)

renda_uk = ancine_mod.loc[ancine_mod['PAIS'] == ' Reino Unido']
renda_uk = renda_uk.RENDA.sum()
renda_uk = np.log10(renda_uk)

#Plotagem em Escala Logarítma de base 10
y = [renda_eua, renda_br, renda_fr, renda_ger, renda_uk]
x = ['Estados Unidos da América', 'Brasil', 'França', 'Alemanha', 'Reino Unido']


plt.barh(x, y, color = 'blue')
plt.title('Renda Acumalada X Top 5 Países de Origem mais ofertados (2009 a 2018)')

#Descriminando os gêneros mais ofertados
genero = ancine_mod['GENERO'].value_counts()
genero.index # Ficção, Documentário, Animação e Videomusical

#Filtragem do gênero em função do público
ficcao = ancine_mod.loc[ancine_mod['GENERO'] == 'Ficção']
ficcao = ficcao.PUBLICO.sum()
ficcao = np.log10(ficcao)

doc = ancine_mod.loc[ancine_mod['GENERO'] == 'Documentário']
doc = doc.PUBLICO.sum()
doc = np.log10(doc)

animacao = ancine_mod.loc[ancine_mod['GENERO'] == 'Animação']
animacao = animacao.PUBLICO.sum()
animacao = np.log10(animacao)

vid_musical = ancine_mod.loc[ancine_mod['GENERO'] == 'Vídeomusical']
vid_musical = vid_musical.PUBLICO.sum()
vid_musical = np.log10(vid_musical)

#Plotagem em Escala Logarítma de base 10
y = [ficcao, doc, animacao, vid_musical]
x = ['Ficção', 'Documentário', 'Animação', 'Videomusical']

plt.barh(x, y, color = 'red')
plt.title('Público Acumulado X Gênero de Filme (2009 a 2018)')

#Descriminando os 10 filmes mais ofertados
filme = ancine_mod['TITULO'].value_counts()
filme.index # Relatos Selvagens(fm01), Medos Privados em Lugares Públicos(fm02), O Menino e o Mundo(fm03), 
            # O Pequeno Nicolau(fm04) O Grilo Feliz e os Insetos Gigantes(fm05), Hanami - Cerejeiras em Flor(fm06),
            # Deixa Ela Entrar(fm07), Um Mar de Aventuras(fm08), Vincere(fm09), Tatuagem(fm10)
            
# Filtragem do filme em função do público
fm01 = ancine_mod.loc[ancine_mod['TITULO'] == 'RELATOS SELVAGENS']
fm01 = fm01.PUBLICO.sum()

fm02 = ancine_mod.loc[ancine_mod['TITULO'] == 'MEDOS PRIVADOS EM LUGARES PUBLICOS']
fm02 = fm02.PUBLICO.sum()

fm03 = ancine_mod.loc[ancine_mod['TITULO'] == 'O MENINO E O MUNDO']
fm03 = fm03.PUBLICO.sum()

fm04 = ancine_mod.loc[ancine_mod['TITULO'] == 'O PEQUENO NICOLAU']
fm04 = fm04.PUBLICO.sum()

fm05 = ancine_mod.loc[ancine_mod['TITULO'] == 'O GRILO FELIZ E OS INSETOS GIGANTES']
fm05 = fm05.PUBLICO.sum()

fm06 = ancine_mod.loc[ancine_mod['TITULO'] == 'HANAMI - CEREJEIRAS EM FLOR']
fm06 = fm06.PUBLICO.sum()

fm07 = ancine_mod.loc[ancine_mod['TITULO'] == 'DEIXA ELA ENTRAR']
fm07 = fm07.PUBLICO.sum()

fm08 = ancine_mod.loc[ancine_mod['TITULO'] == 'UM MAR DE AVENTURAS']
fm08 = fm08.PUBLICO.sum()

fm09 = ancine_mod.loc[ancine_mod['TITULO'] == 'VINCERE']
fm09 = fm09.PUBLICO.sum()

fm10 = ancine_mod.loc[ancine_mod['TITULO'] == 'TATUAGEM']
fm10 = fm10.PUBLICO.sum()

#Plotagem
y = [fm01, fm02, fm03, fm04, fm05, fm06, fm07, fm08, fm09, fm10]
x = ['RELATOS SELVAGENS', 
     'MEDOS PRIVADOS EM LUGARES PUBLICOS', 
     'O MENINO E O MUNDO', 
     'O PEQUENO NICOLAU',
     'O GRILO FELIZ E OS INSETOS GIGANTES',
     'HANAMI - CEREJEIRAS EM FLOR',
     'DEIXA ELA ENTRAR',
     'UM MAR DE AVENTURAS',
     'VINCERE',
     'TATUAGEM']

plt.barh(x, y, color = 'purple')
plt.title('Público Acumulado X Top 10 Filmes Mais Ofertados - 2009 a 2018')