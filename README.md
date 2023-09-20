Nama          : Muhamad Hanif Nurrifky Wicaksono

Kelas         : PBP-F

Link Domain   : https://muhamadhanifnurrifky-pbp.adaptable.app/

Pertanyaan Tugas-2:
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). <br>
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
   
3. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.<br>
   Jawab:
   ![Bagan Tugas2PBP](https://github.com/HanifRifky/TugasPBP2/assets/114400903/d8efca74-aea7-4ca9-9a5b-2b7ba381954c)
   
4. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?<br>
   Jawab:
   - Virtual Environment bermanfaat untuk memisahkan dependensi antar proyek dan menghindari konfilk antar proyek tersebut.
   - Kita tetap bisa membuat aplikasi web dengan django tanpa menggunakan VE. Namun, bisa saja terjadi konflik pada proyek sehingga, hal tersebut bukan merupakan "best practice"
     
5. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.<br>
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
  
Pertanyaan Tugas-3:<br>
1. Apa perbedaan antara form POST dan form GET dalam Django?<br>
   Jawab:
   - POST : Request yang mengubah data dari database, biasanya menggunakan POST
   - GET  : Mengubah data yang dimasukkan menjadi string dan menggabungkannya ke dalam URL
  
2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?<br>
   Jawab:
   - XML   : XML menyimpan, menyusun, dan mengorganisir data secara terstruktur untuk pertukaran data antar aplikasi. Cukup fleksibel dan dapat menyesuaikan dengan tipe struktur data yang             dikirim
   - JSON  : JSON adalah format data yang penulisannya cukup ringkas sehingga mudah dibaca. Cocok untuk mengirimkan data dari server (database) ke halaman web dan lebih mudah untuk                     mengirim data dengan struktur array.
   - HTML  : Lebih kepada markup language yang bertujuan untuk memberikan desain pada halaman web atau aplikasi
  
3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?<br>
   Jawab:
   karena format dari JSON sendiri yang ringkas dan mudah dibaca sehingga memudahkan programmer dan menyusun data. JSON juga kompatibel dan sejalan dengan berbagai bahasa pemrograman         lainnya sehingga mudah bagi programmer untuk menghubungkan sebuah data ke aplikasi atau web dengan bahasa pemrograman yang beragam. Bandwith yang digunakan juga kecil sehingga JSON        cukup ringan saat ingin mengirim data yang cukup besar.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)<br>
   jawab:
   - Membuat berkas baru bernama forms.py di direktori main dan mengimport beberapa modul seperti ModelForm dari django .forms dan Product dari main.models. Serta menginisiasi class            ProductForm.
   - import HttpResponseRedirect, ProductForm dari main.forms, dan reverse ke dalam views.py
   - Membuat fungsi baru bernama create_product untuk menerima parameter request. Digunakan saat user dari web atau aplikasi mengisi form.
   - Menambahkan object product pada fungsi show_main agar apa yagn dimasukkan di form, bisa dilihat.
   - import fungsi show_main dan create_product ke urls.py di main
   - Membuat create_product.html agar bisa menampilkan form
   - membuat fungsi show_xml, show_json, show_xml_by_id, dan show_json_by_id agar bisa melihat data2 yang dimasukkan melalui form melalui parameter data yang berbeda.
   - memasukkan setiap link parameter data ke dalam postman agar bisa menyelesaikan checklist terakhir

5. ScreenShot postman<br>
   - Postman HTML <br>
   ![postman HTML](https://github.com/HanifRifky/TugasPBP2/assets/114400903/d4d7e806-2f45-45ec-ba21-0ac80bc2e613) <br>

   - Postman XML <br>
   ![xml](https://github.com/HanifRifky/TugasPBP2/assets/114400903/4dc79f8e-185d-44a5-8dc3-3992b722bf27) <br>

   - Postman JSON <br>
   ![json](https://github.com/HanifRifky/TugasPBP2/assets/114400903/48edec15-b7a5-41b5-bb48-08ae8e23a61e) <br>

   - postman XML by id <br>
   ![xml_Id](https://github.com/HanifRifky/TugasPBP2/assets/114400903/f32d5747-adf2-41ee-a21a-a60c8c43c4c7) <br>

   - postman JSON by id <br>
   ![json_Id](https://github.com/HanifRifky/TugasPBP2/assets/114400903/87c06d33-e3ad-4794-a9a3-e6dd2e24b396) <br>
   
   
   
   
   
   
      
