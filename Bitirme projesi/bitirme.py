from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Konulara göre cevaplar
yanitlar = {
    "üçgen açıları": {
        "soru": ["üçgen açıları nedir", "üçgenin iç açıları", "üçgenin açıları toplamı", "üçgenin açıları"],
        "cevap": "Bir üçgenin iç açıları toplamı her zaman 180°'dir. Üçgenin her üç açısının toplamı 180° eder."
    },
    "bir bilinmeyenli denklem": {
        "soru": ["bir bilinmeyenli denklem nedir", "bir bilinmeyenli denklem örneği", "x nedir"],
        "cevap": "Bir bilinmeyenli denklem, içinde sadece bir bilinmeyen bulunan bir denklem türüdür. Örneğin, '2x + 3 = 7' denklemi bir bilinmeyenli denklemdir."
    },
    "sözcükte anlam": {
        "soru": ["sözcükte anlam nedir", "kelimenin anlamı", "sözcük anlamı"],
        "cevap": "Sözcükte anlam, bir kelimenin dilde taşıdığı anlamı ifade eder. Sözcüklerin farklı anlamları olabilir, bağlama göre anlam değişebilir."
    },
    "armut": {
        "soru":["armut nedir", "armut"],
        "cevap":[" Gülgillerden, Çiçekleri Beyaz, Türkiye'nin Her Yerinde Yetişen Bir Ağaç (Pirus Communis), Bu Ağacın Tatlı Ve Sulu, Yumuşak, Ufak Çekirdekli Meyvesi, Çok Bön, Çok Aptal"]

    }
}

# Anasayfa
@app.route('/')
def index():
    return render_template('index.html')

# Chatbot yanıtlarını sağlayan API
@app.route('/get_response', methods=['POST'])
def get_response():
    try:
        data = request.get_json()  # Gelen JSON verisini al
        user_input = data['message'].strip().lower()  # Kullanıcı mesajını al ve küçük harfe çevir

        response = None
        # Gelen mesajı her konu başlığıyla kontrol et
        for konu, bilgiler in yanitlar.items():
            for soru in bilgiler["soru"]:
                # Eğer soruda geçen kelimeler kullanıcının sorusunda varsa cevabı ver
                if soru in user_input:
                    response = bilgiler["cevap"]
                    break

            if response:
                break

        if response is None:
            response = "Üzgünüm, bu konuda bilgiye sahip değilim. Üçgen açıları, bir bilinmeyenli denklemler, veya sözcükte anlam konularında yardımcı olabilirim."
        
        # Cevabı JSON formatında geri gönder
        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"response": "Bir hata oluştu. Lütfen tekrar deneyin."})


if __name__ == '__main__':
    app.run(debug=True)
