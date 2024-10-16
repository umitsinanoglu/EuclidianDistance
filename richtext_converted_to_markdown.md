EuclideanDistance
=================

Bu proje, iki nokta arasındaki **Öklidyen Mesafeyi (Euclidean Distance)** hesaplamak için geliştirilmiştir. Matematikte, Öklidyen mesafe, iki nokta arasındaki "doğru çizgi" boyunca olan en kısa uzaklığı temsil eder. Bu araç, özellikle makine öğrenimi ve veri analizi uygulamalarında yaygın olarak kullanılır.

🔧 Kurulum
----------

Proje kodunu bilgisayarınıza klonlamak için aşağıdaki adımları izleyin:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashKodu kopyala# Projeyi klonlayın  git clone https://github.com/umitsinanoglu/EuclidianDistance.git  # Proje dizinine gidin  cd EuclidianDistance   `

🛠️ Gereksinimler
-----------------

Bu proje, temel Python kütüphanelerine dayanmaktadır. Aşağıdaki komutla bağımlılıkları kurabilirsiniz:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashKodu kopyalapip install -r requirements.txt   `

> **Not:** Eğer requirements.txt yoksa, temel olarak Python 3.x yeterlidir.

🚀 Kullanım
-----------

euclidean\_distance.py dosyası, iki nokta arasındaki Öklidyen mesafeyi hesaplayan bir fonksiyon içerir. Aşağıdaki örnek kodu kullanarak çalıştırabilirsiniz:

### Örnek Kod

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pythonKodu kopyalafrom euclidean_distance import calculate_distance  # İki nokta arasındaki mesafe hesaplanıyor  point1 = (1, 2)  point2 = (4, 6)  distance = calculate_distance(point1, point2)  print(f"İki nokta arasındaki Öklidyen mesafe: {distance}")   `

### Beklenen Çıktı

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   yamlKodu kopyalaİki nokta arasındaki Öklidyen mesafe: 5.0   `

📁 Proje Yapısı
---------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashKodu kopyalaEuclidianDistance/  │  ├── euclidean_distance.py  # Mesafe hesaplama fonksiyonunu içerir  ├── requirements.txt       # Bağımlılıkların listesi (eğer gerekli ise)  └── README.md              # Proje hakkında bilgi   `

🧮 Formül
---------

Öklidyen Mesafe Formülü:

d=(x2−x1)2+(y2−y1)2d = \\sqrt{(x\_2 - x\_1)^2 + (y\_2 - y\_1)^2}d=(x2​−x1​)2+(y2​−y1​)2​

Burada:

*   ddd = Öklidyen mesafe
    
*   (x1,y1)(x\_1, y\_1)(x1​,y1​) ve (x2,y2)(x\_2, y\_2)(x2​,y2​) = İki noktanın koordinatları
    

📝 Katkıda Bulunma
------------------

Katkıda bulunmak isterseniz:

1.  Projeyi forklayın.
    
2.  Bir branch oluşturun: git checkout -b yeni-özellik.
    
3.  Değişikliklerinizi commit edin: git commit -m 'Özellik eklendi'.
    
4.  Branch'e push edin: git push origin yeni-özellik.
    
5.  Bir **Pull Request** açın.
    

📄 Lisans
---------

Bu proje MIT Lisansı kapsamında lisanslanmıştır.

🤝 İletişim
-----------

Herhangi bir sorunuz veya öneriniz varsa, benimle iletişime geçmekten çekinmeyin:

*   **Geliştirici:** Ümit Sinanoğlu