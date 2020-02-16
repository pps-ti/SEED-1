Panduan <i>deploy</i> ke Heroku dapat dilihat di <a href="https://drive.google.com/file/d/1k8bpOPOez_-xFUzD3aJFGiaEVgegL3Mu/view?usp=sharing">sini</a>.

Cara menjalankan pada <i>debug mode</i> :<br>
<b>OPSI PERTAMA</b>
1. Tambahkan potongan kode ```app.run(debug=True)``` pada baris yang terbawah pada <a href="https://github.com/pps-ti/SEED-1/blob/master/flaskweb/main.py" target="blank">main.py</a> tanpa indentasi. Kalau kalian bingung silahkan cek peletakannya pada <a href="https://github.com/pps-ti/SEED-1/blob/master/File%20Presentasi.pdf" target="blank"><i>slide</i> terakhir presentasi</a>.
2. Buka terminal/cmd kalian pada direktori ini kemudian ketik ```python main.py```

Jika tidak berhasil maka kata-kata ```python``` pada poin kedua dapat diganti dengan ```py``` atau ```python3```<br>

<b>OPSI KEDUA</b>
1. Buka terminal/cmd kalian pada direktori ini
2. Ketik ```set FLASK_APP=main.py```
3. Dilanjutkan dengan ketik ```set FLASK_ENV=development```
4. Terakhir ketik ```flask run```

Jika kalian menggunakan linux, maka kata-kata ```set``` dapat diganti dengan ```export```
