Nama          : Muhamad Hanif Nurrifky Wicaksono

Kelas         : PBP-F

Link Domain   : https://muhamadhanifnurrifky-pbp.adaptable.app/

**PERTANYAAN TUGAS-2:** <br>
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
  
**PERTANYAAN TUGAS-3**:<br>
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
   
   
**PERTANYAAN TUGAS-4:**<br>
1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?<br>
   UserCreationForm merupakan sebuah template yang telah disediakan oleh django untuk membuat semacam formulir registrasi pengguna. Isinya terdapat usernam, password, dan email.<br>
   Kelebihan : Mudah digunakan, terintegrasi dengan Django Authentication System, dan Dapat otomatis memvalidasi masukkan user. <br>
   Kekurangan : Tidak dapat diubah secara berlebihan, harus menambahkan informasi selain yang disediakan secara manual, dan tidak otomatis terhubung dengan front-end suatu aplikasi atau web. <br>
<br>
2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?<br>
   > Autentikasi : Proses verifikasi data-data user. Contohnya adalah saat user ingin login dan memasukkan data-datanya, autentikasi memeriksa apakah data-data tersebut sesuai dengan data-data yang ada di database. Dalam django, hal ini berkaitan dengan User model dan UserCreationForm.<br>
   > Otorisasi : Mengontrol akses user ke beberapa bagian dan/atau fungsi dari sebuah aplikasi atau web. Contohnya adalah saat user sudah masuk ke aplikasi atau web, sistem akan memeriksa user tersebut memiliki akses ke fitur dan/atau bagian mana saja dari sebuah aplikasi. Django sendiri memiliki beberapa fungsi untuk melakukan otorisasi ini seperti fungsi "@login_required" yang meminta agar user harus login terlebih dulu sebelum melanjutkan.<br>
<br>
3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?<br>
   >Cookies : merupakan sebuah mekanisme yang dapat menyimpan suatu data berukuran kecil secara sementara pada sisi klien. Cookies biasanya digunakan untuk menyimpan data pada perangkat user sehingga jika suatu saat informasi tersebut dibutuhkan, data tersebut bisa diakses dan digunakan kembali.<br>
   >Cookies in Django :<br>
      - Memulai session : Django akan menyimpan sebuah id unik saat user masuk pertama kali ke dalam web<br>
      - Penyimpanan data sesi : Django akan menyimpan data-data seperti informasi-informasi login user dan disimpan pada server tapi identifikasi sesinya disimpan di perangkat user.<br>
      - Menggunakan Cookie : Setelah semuanya disimpan, server django akan mengirim id sesi ke perangkat user dalam bentuk cookie. Sehingga, setiap kali user masuk ke halaman web tadi, cookie tadi akan dikirimkan kembali ke server sebagai request HTTP.<br>
      - Pemulihan data sesi : ketika server menerima permintaan tadi, ia akan mengidentifikasi sesi user dan mengambil data yang diperlukan.<br>
      - Penghapusan sesi seusai durasi : Django juga dapat mengatur sesi pengguna untuk berakhir jika pada periode tertentu, tidak ada aktivitas sama sekali dari user.<br>
<br>
4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?<br>
   > Resiko Cookies :<br>
     - Resiko keamanan : Informasi yang di ambil dan disimpan, bisa saja mengandung data sensitif. Sehingga data-data tersebut harus dienkripsi dan hanya digunakan untuk komunikasi antara perangkat user dan server saja.<br>
     - Resiko Penyusupan (Hijacking) : Orang lain bisa saja mencuri session ID yang unik tadi dan digunakan untuk mengakses akun user tanpan izin. Bisa dicegah dengan cara menggunakan fitur keamanan seperti HttpOnly atau SecureFlags.<br>
     - Cookies dari sumber sembarangan : Jika menggunakan dan menerima cookies yang sumbernya tidak diketahui, hal ini dapat membuka pintu serangan keamanan data dari berbagai sisi.<br>
<br>
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).<br>
   > Import beberapa modul seperti redirect, UserCreationForm (membuat form registrasi user), dan messages pada berkas views.py.<br>
   > Membuat fungsi yang regsiter agar user bisa melakukan regsitrasi data pengguna pada aplikasi web<br>
   > membuat fungsi login agar user bisa masuk ke halaman web setelah memasukkan data-data user<br>
   > Membuat fungsi logout agar user bisa keluar dari halaman web<br>
   > Membuat berkas register.html yang isinya merupakan tabel-tabel untuk menginput data registrasi user<br>
   > Membuat berkas login.html yang berguna untuk membuat tabel-tabel untuk menginput data login bagi user<br>
   > Membuat tombol logout pada berkas main.html<br>
   > Mengimport semua fungsi (register, login, dan logout) dari views.py ke urls.py serta menambahkan path untuk semua fungsi tersebut.<br>
   > Menambahkan fitur "@login required" agar setiap user yang ingin masuk ke dalam halaman web, harus di autentikasi dan di otorisasi terlebih dulu data-datanya.<br>
   > Menambahkan fitur-fitur Cookies seperti "last_login" yang dapat mengembalikan data kapan terakhir kali user tersebut mengakses halaman web tersebut.<br>
   > menyesuaikan kembali fungsi-fungsi register, login, dan logout agar sesuai dengan fitur-fitur cookies.<br>
   > Mencoba hasil halaman web dengan cara menginput dua user ke dalam halaman web.<br>
   > Menghubungkan model product dengan user<br>


**PERTANYAAN TUGAS-5:**<br>
1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.<br>
   Jawab:<br>
   Secara garis besar, element selector disesdiakan oleh CSS (CSS Selectors) untuk memisahkan berbagai elemen saat ingin diberikan style tertentu. Contoh element Selector:
      - Simple selectors (berdasarkan name, id, class) - digunakan jika ada element spesifik yang telah diberikan karakteristik berbeda.<br>
      - Combinator selectors (hubungan spesifik) - Digunakan saat ada beberapa elemen yang memiliki kesamaan karakteristik<br>
      - Pseudo-class selectors (Berdasarkan kondisi) - Digunakan saat ada beberapa elemen yang memiliki kondisi-kondisi yang mirip<br>
      - Pseudo-elements selctors (Sedikit bagian dari elemen) - Digunakan saat ingin mengubah style dari beberapa bagian dari suatu elemen<br>
      - Attribute selectors (atribut elemen) - Digunakan saat mengubah suatu atribut dari suatu elemen<br>
<br>
2. Jelaskan HTML5 Tag yang kamu ketahui.<br>
   Jawab:<br>
   - "<Header>" = Menunjukkan bagian atas dari sebuah dokumen html. Berisi link2 dan elemen2 lain yang berkaitan dengan halaman secara tidak langsung.<br>
   - "<Nav>" = Menunjukkan dan digunakan saat ingin membuat navigasi halaman<br>
   - "<section>" = Membagi beberapa bagian dari dokumen html<br>
   - "<input>" = Mengisi input <br>
<br>
3. Jelaskan perbedaan antara margin dan padding.<br>
   Jawab:<br>
   A. Margin<br>
      Merupakan ruang di luar dari sebuah elemen HTML. Mengontrol jarak antar elemen. Tidak memiliki atribut latar belakang maupun "border" dan hanya bisa digunakan untuk membuat ruang dan jarak antar elemen. Margin bersifat transparan, yang berarti jika ada dua elemen yang memiliki margin sama, maka akan diambil salah satu margin saja.<br>
   B. Padding<br>
   Merupakan ruang di dalam suatu elemen HTMl dan terletak di antara batas elemen dan konten di dalam elemen tersebut. Megontrol jarak antara konten dari batas elemennya. Padding tidak bersifat transparan dan akan diterapkan secara terpisah.<br>
<br>
4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?<br>
   Jawab:
   A. Tailwind CSS<br>
      Tailwind menyediakan sejumlah besar class style yang bisa digunakan langsung ke dalam HTML tanpa harus membuat rancangan style CSS secara terpisah. Tingkat fleksibilitas dari tailwind juga cukup luas sehingga, cocok dogunakan jika ingin mengontrol tampilah lebih leluasa.<br>
   B. Bootstrap<br>
      Merupakan framework CSS yang lebih tradisional dan berorientasi pada komponen2 dasar dari CSS itu sendiri. Bootstrap sendiri digunakan dengan cara menggabungkan markup HMTL dengan class bootstrap yang telah disesuaikan sebelumnya. Cocok digunakan bagi yang ingin lebih berorientasi pada komponen2 tertentu. Bootstrap juga cocok jika ingin cepat membangun tampilan depan dari web/aplikasi.<br>
<br>
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).<br>
   Jawab:
   - import link2 Framework CSS(bootstrap, tailwind) ke dalam head di base.html
   - mengubah format login yang awalnya hanya fokus ke tabel, menjadi format "<div>"
   - Mengaplikasikan beberapa template login dan mengubah2 template sedikit

## Pertanyaan Tugas 6 <br>

   

   
   
   
   
      
