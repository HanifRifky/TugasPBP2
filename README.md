Nama          : Muhamad Hanif Nurrifky Wicaksono

Kelas         : PBP2-F

Link Domain   : https://muhamadhanifnurrifky-pbp.adaptable.app/

Pertanyaan:
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   Jawab:
   - Yang pertama dilakukan pastinya membuat folder/direktori lokal dengan nama tugasPBP2.
   - Buat juga repositori di GitHub untuk menyimpan folder tugasPBP2
   - Menyalakan virtual evironment dan membuat dile dependencies untuk menginstall Django di folder tugasPBP2
   - Menambahkan aplikasi main di direktori tugasPBP2 yang nantinya akan menjadi page utama dari web yang dibentuk
   - Menambahkan main.html yang berisi program html tentang tampilan pada layar website
   - Membuat models.py yang merupakan kelas dasar dari model dalam Django. Di dalamnya terdapat atribut2 dan field sesuai yang diminta pada tugas
   - Menhubungkan view dengan template dengan cara membentuk views.py yang berisi program isi dari field atribut
   - Membuat urls.py pada aplikasi dan proyek. "urls.py" pada plikasi mengatur rute spesifik dari fitur2 pada aplikasi. Sedangkan urls.py pada proyek mengarahkan rute url tingkat proyek dan memungkinkan proyek django bersifat terpisah
   - Mebuat dan menjalankan unit test
   - Deploy aplikasi web di Adaptable.io
   
3. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
   Jawab:
   ![Bagan Tugas2PBP](https://github.com/HanifRifky/TugasPBP2/assets/114400903/d8efca74-aea7-4ca9-9a5b-2b7ba381954c)
   
4. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
   Jawab:
   - Virtual Environment bermanfaat untuk memisahkan dependensi antar proyek dan menghindari konfilk antar proyek tersebut.
   - Kita tetap bisa membuat aplikasi web dengan django tanpa menggunakan VE. Namun, bisa saja terjadi konflik pada proyek sehingga, hal tersebut bukan merupakan "best practice"
     
5. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
   Jawab:
   A. MVC (Model-View-Controller)
      - Model       : Bergerak di area "database". Tidak memiliki program tentang interface sama sekali. Bertanggungjawab mengatasi domain dan komunikasi antar database dan jaringan
      - View        : Merupakan User Interface. Merupakan visualisasi dari data2 yang ada di models.
      - Controller  : Membentuk koneksi antar view dan models. Berisi program inti yang mengambil respon user dan memberikan timbal balik dari model
   B. MVT (Model-View-Template)
      - Variasi dari MVC oleh Framework django
      - Model       : Mirip seperti model di MVC. Model di MVT menjadi logika dasar dari aplikasi yang dibentuk dan direpresentasikan oleh database tertentu
      - View        : Sama seperti view di MVC. Merupakan UI dan komponen-komponen yang terlihat di browser website atau aplikasi
      - Template    : Static kode dari sebuah HTML, mirip seperti view di MVT.
   C. MVVM (Model-View-ViewModel)
      - Model       : Bertanggungjawab atas sumber-sumber data
      - View        : Tampilan interface dari program. Bagian ini tidak terdapat aplikasi logika sama sekali
      - ViewModel   : Menghubungkan antara View dan Model.
  
   D. Perbedaan ketiganya
      - Perbedaan utamanya terletak di Controller, Template, dan ViewModel di ketiganya. Hal ini tentunya membedakan fungsi "controlling" web dan aplikasi dengan user.
      - MVVM juga mendukung two-way data binding yang membuat sinkronisasi antara view dan viewModel lebih otomatis dibandingkan ketiga model lainnya.
      - MVT dan MVC lebih berfokus pada web yang banyak berkutat dengan akses satu arah. Sedangkan MVVM berkecimpung pada aplikasi dua arah seperti aplikasi chat.
   
      
