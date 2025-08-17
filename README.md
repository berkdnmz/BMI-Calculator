# BMI Calculator

A simple desktop application developed using Python and the Tkinter library to help users 
calculate their Body Mass Index (BMI) and understand their weight category.
It offers a clean and user-friendly interface suitable for users of all ages.
---
## Table of Contents

- [English Section](#bmi-calculator)
- [Türkçe Bölüm](#bmi-calculator-tr)
---
## Contents

- [Overview](#overview)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [File Structure](#file-structure)  
- [License](#license)
---
## Overview

This project is a desktop application developed with Python and Tkinter 
that calculates the Body Mass Index (BMI) based on the user’s height and weight.
The application automatically categorizes the BMI into standard ranges such as 
Underweight, Normal, Overweight, or Obese, and displays the result clearly.

Thanks to its simple interface, users of all ages can easily enter their data and 
receive instant feedback.

---
## Features

### Current Features
- User-friendly interface built with `Tkinter`
- Height and weight input
- BMI calculation and classification
- Instant result display with BMI value and category
- Basic error handling for empty or invalid input

### Planned Features
- Support for multiple measurement units (kg/cm, lb/inch)
- History tracking of previous BMI calculations
- Customizable themes and fonts
- Enhanced error popups and animations
- Advanced statistics and visualization
---
## Installation
1. **Clone the repository**  
```bash
git clone https://github.com/berkdnmz/BMI-Calculator.git  
cd BMI-Calculator
```

2. **Check Python version**  
Python 3.10 or higher is recommended. 
```bash
python --version  
```

3. **Install dependencies**  
`tkinter` usually comes pre-installed with Python. If there are additional packages, you can install them from the `requirements.txt` file.  
```bash
pip install -r requirements.txt  
```

4. **Start the application**  
```bash
python main.py  
```
---
## Usage
1. Run `main.py` in terminal or command prompt.

```bash
python main.py
```
2. Enter your **height** in centimeters and **weight** in kilograms.

3. Press the **Enter**.

3. The application will display:
    - Your **BMI value** (rounded to 1 or 2 decimal places)
    - Your **weight** category (Underweight, Normal, Overweight, Obese)
4. If any field is empty or invalid, an error message will appear.

### Future updates may include:  
- Different game modes (Turkish → English),
- Calculation history and statistics,  
- Customizable UI settings.

---
## File Structure
```
BMI-Calculator/
│
├── main.py          # Main application entry point
├── calculator.py    # BMI calculation and classification logic
├── gui.py           # User interface and event handling
├── LICENSE          # License file
└── README.md        # Project documentation
```
---

## License

This project is open source under the [MIT License](LICENSE).  
You are free to use, modify, and distribute it as you wish — however, you must credit the original author.

---
## Project Owner

**Berk DÖNMEZ**

GitHub: [github.com/berkdnmz](https://github.com/berkdnmz)  
LinkedIn: [linkedin.com/in/berkdnmz](https://linkedin.com/in/berkdnmz)  

For any questions or suggestions about the project, feel free to contact me.
**Happy coding and stay healthy!**

---

# BMI Calculator [TR]
Python ve Tkinter kullanılarak geliştirilmiş, kullanıcıların Boy Kitle İndeksini (BMI) hesaplamasını ve kilo kategorilerini öğrenmesini sağlayan basit bir masaüstü uygulamasıdır.
Sade ve anlaşılır arayüzü sayesinde her yaş grubundan kullanıcı için uygundur.

---

## İçindekiler

- [Genel Bakış](#genel-bakış)  
- [Özellikler](#özellikler)  
- [Kurulum](#kurulum)  
- [Kullanım](#kullanım)  
- [Dosya Yapısı](#dosya-yapısı)
- [Lisans](#Lisans)

---

## Genel Bakış

Bu proje, Python ve Tkinter kullanılarak geliştirilmiş, kullanıcıların boy ve 
kilo bilgilerini girerek BMI hesaplamasına olanak tanıyan bir masaüstü uygulamasıdır.

Uygulama, BMI değerini otomatik olarak kategorize eder 
(Zayıf, Normal, Fazla Kilolu, Obez) ve sonucu net bir şekilde gösterir.
 

Basit arayüzü sayesinde kullanıcılar kolayca veri girişi yapabilir ve anında sonuç alabilir.

---

## Özellikler

### Mevcut Özellikler
- `Tkinter` tabanlı **kullanıcı dostu arayüz**
- Boy ve kilo giriş alanları
- BMI hesaplama ve sınıflandırma
- Anlık sonuç gösterimi (BMI değeri ve kategori)
- Boş veya geçersiz girişler için basit hata kontrolü

### Planlanan Özellikler
- Farklı ölçü birimlerini destekleme (kg/cm, lb/inch)
- Önceki BMI hesaplarının kaydı ve istatistikler
- Tema ve font kişiselleştirme
- Geliştirilmiş hata popup’ları ve animasyonlar
- İleri düzey istatistik ve görselleştirme

---

## Kurulum

1. **Depoyu klonlayın**  
```bash
git clone https://github.com/berkdnmz/BMI-Calculator.git  
cd BMI-Calculator
```

2. **Python sürümünü kontrol edin**  
Python 3.10 veya üzeri önerilir.
```bash
python --version  
```

3. **Gereksinimleri Kurun**  
`tkinter` çoğu Python kurulumunda ön yüklüdür.
    - Ek paketler varsa:
```bash
pip install -r requirements.txt  
```

4. **Uygulamayı başlatın**  
```bash
python main.py  
```
---
## Kullanım

1. Terminal veya komut satırında `main.py` dosyasını çalıştırın.

```bash
python main.py
```
2. Boyunuzu cm cinsinden ve kilonuzu kg cinsinden girin.
3. Enter tuşuna basın.
4. Uygulama size gösterecek:
    - BMI değeri (1 veya 2 ondalık basamak)
    - Kilo kategorisi (Zayıf, Normal, Fazla Kilolu, Obez)
5. Boş veya geçersiz giriş yapılırsa ekranda hata mesajı görünecektir.


### İlerleyen sürümlerde;  
- Farklı ölçü birimleri (lb/inch),
- Hesaplama geçmişi ve istatistikler, 
- Özelleştirilebilir arayüz ayarları.

---

## Dosya Yapısı

```
BMI-Calculator/
│
├── main.py          # Uygulamanın ana çalıştırma dosyası
├── calculator.py    # BMI hesaplama ve sınıflandırma mantığı
├── gui.py           # Arayüz tasarımı ve olay yönetimi
├── LICENSE          # Lisans dosyası
└── README.md        # Proje dökümantasyonu
```
---
## Lisans

Bu proje [MIT Lisansı](LICENSE) kapsamında açık kaynak olarak sunulmuştur.  
Dilediğiniz gibi kullanabilir, değiştirebilir ve paylaşabilirsiniz — ancak orijinal geliştiriciyi belirtmeniz gerekir.

---

## Proje Sahibi

**Berk DÖNMEZ**

GitHub: [github.com/berkdnmz](https://github.com/berkdnmz)  
LinkedIn: [linkedin.com/in/berkdnmz](https://linkedin.com/in/berkdnmz)  

Projeyle ilgili her türlü soru ve öneri için bana ulaşabilirsiniz.  



**İyi çalışmalar ve sağlıklı kalın!**
