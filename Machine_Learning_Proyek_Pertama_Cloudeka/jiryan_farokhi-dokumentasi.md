# Submission 1: Sentiment Analys 
Nama: Jiryan Farokhi

Username dicoding: jiryan_farokhi

| | Deskripsi |
| ----------- | ----------- |
| Dataset | [Review Content Analyst](https://www.kaggle.com/competitions/internal-selection-satria-data)|
| Masalah | Dalam Dataset ini terdapat data review content dari para user dari data review tersebut sulit untuk menentukan apakah review content tersebut negatif atau positif karena terdapat review dengan 1500 data review |
| Solusi machine learning | Machine Learning menghadirkan solusi dengan deteksi otomatis dalam data dengan menggunakan pendekatan Natural Language Processing yang diproses dengan model LSTM serta memanfaatkan machine learning pipeline untuk mengotomatiskan alur kerja pembelajaran mesin dari mulai preprocessing sammpai pengujian model agar dapat lebih terstruktur, efisien, dan mudah diulang  |
| Metode pengolahan | Metode pengelolahan data yang digunakan yaitu tokenisasi sebagai fitur input, data awal yang berupa text akan dilakukan data cleansing. Serta normalisasi data label dengan LabelEncoding untuk menjaga agar kualitas data tettap terjaga |
| Arsitektur model | Model ini dibangun menggunakan layer TextVectorization, sebagi layer yang berfungsi untuk memproses input string kedalam bentuk angka, dan layer embedding bertugas untuk mengukur kedekatan atau kesamaan dari setiap kata untuk mengetahui kata tersebut merupakan kata negatif atau kata positif. Serta model compile menggunakan Binary Crossentropy Adam dengan learning_rate 0.01 dan metrics BinaryAccuray |
| Metrik evaluasi | Mertrik evaluasi yang di gunakan pada model ini yaitu TP, TN, FP, dan FN |
| Performa model | Evaluasi model diperoleh yaitu AUC sebesar 68%, kemudian example_count 281, dengan BinaryAccuracy 62%, dan loss sebesar 1.816. Untuk False Negatives 50, False Positive 55, True Negative 79 dan True Positive 97. Model yang telah dibuat dapat dilakukan peningkatan performa, karena model belum cukup baik karena BinaryAccuracy masih dibawah 80% |
