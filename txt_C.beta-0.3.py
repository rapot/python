import fnmatch
import os
import shutil


disk = True


while disk:
    wherefind=input('Введите диск на котором ищём: ') 
    dir=wherefind

    if wherefind == 'e:':      
         disk = False # это останавливает цикл while
    elif wherefind == 'd:':
         disk = False
    elif wherefind == 'c:':
         disk = False     
    
    else:     
      print('Неверная буква, попробуйте ещё раз')


else:
  createdir = input('Введите название папки, если папки нет, она будет создана: ')
  
tip = True
while tip:
    pattern=input('Введите маску "txt", "foto": ')
    if pattern=='txt':
      pattern1=['*.txt','*.xls', '*.xlsx','*.doc', '*.docm','*.rtf','*.odt','*.docx','*.fb2','*.log','*.pdf','*.epub']
      tip=False

    elif pattern=='foto':
      pattern1=['*.png','*.jpeg','*.jpg','*.bmp','*.cpt','*.gif','*.tga','*.psd','*.tiff','*.tif']  
      tip=False
    else:
      print('Неверная маска')
else:
  
  matches=[]
  os.makedirs(createdir) #создать директорию. 
  for root, dirnames, filenames in os.walk(dir):
    for extensions in pattern1:
      for filename in fnmatch.filter(filenames, extensions):
        matches.append(os.path.join(root, filename))
        source=(os.path.join(root, filename))
        shutil.copy(source, createdir)
        print(source)
  
 
ar=True
while ar:
  archive=input('Архивируем ? "y" or "n": ')
  if archive=='y':
    arname=input('Введите имя архива: ')
    ar=False
  elif archive=='n':
    break

  else:
    print('Введите y или n')

else:
  print('Ожидайте окончения работы скрипта, это будет занять продолжительное время')
  shutil.make_archive(arname, 'zip', createdir)
  print('ok')




 

