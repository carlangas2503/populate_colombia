import matplotlib.pyplot as plt
import csv

def populateCol(path):
  data = []
  with open(path) as file:
    reader = csv.reader(file,delimiter=',')
    header = next(reader)
    for line in reader:
      obj = { key:value for (key,value) in zip(header,line)}
      if obj['CCA3'] == 'COL':
        data.append(obj)
  data = data[0]
  data = [i for i in data.items() if 'Population' in i[0] and not 'World' in i[0]]
  data_num = []
  data_age = []
  for ele in data:
    data_num.append(ele[1])
    data_age.append(ele[0])
  print(data_num,data_age)
  
  fig, ax = plt.subplots()
  ax.bar(data_age,data_num)
  plt.show()

if __name__ == '__main__':
  populateCol('./app/data.csv')