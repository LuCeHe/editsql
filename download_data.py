import gdown

id_sparc = '13Abvu5SUMSP3SJM-ZIj66mOkeyAquR73'
id_bert = '1f_LEWVgrtZLRuoiExJa5fNzTS8-WcAX9'

url = 'https://drive.google.com/uc?id={}'.format(id_bert)
output = '20150428_collected_images.tgz'
gdown.download(url)



#'http://nlp.stanford.edu/data/glove.840B.300d.zip'