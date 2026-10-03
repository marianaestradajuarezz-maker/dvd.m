import os
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Davidcito.</title>
    <style>
        body {
            background-color: #fce4ec;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            overflow: hidden;
        }
        .card {
            background-color: #fff5f7;
            border: 2px solid #ffb3c6;
            border-radius: 20px;
            padding: 40px 20px;
            width: 85%;
            max-width: 500px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(255, 179, 198, 0.3);
            position: relative;
        }
        .ribbon {
            font-size: 35px;
            margin-bottom: 10px;
            color: #ff4d6d;
        }
        .title {
            color: #ff4d6d;
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 25px;
        }
        .verse-container {
            border: 1px dashed #ffb3c6;
            border-radius: 12px;
            padding: 20px 15px;
            margin-bottom: 20px;
            background-color: #fffdfd;
            min-height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .verse {
            color: #c9184a;
            font-size: 20px;
            font-weight: bold;
            line-height: 1.5;
            margin: 0;
        }
        .gif-box {
            margin-bottom: 20px;
            min-height: 180px;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .gif-box img {
            max-width: 180px;
            max-height: 180px;
            border-radius: 15px;
            object-fit: cover;
        }
        .btn-container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 15px;
            min-height: 100px;
            position: relative;
        }
        .btn {
            color: white;
            border: none;
            border-radius: 25px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, background-color 0.2s;
            display: inline-block !important;
        }
        .btn-yes {
            background-color: #2a9d8f;
            padding: 12px 35px;
            font-size: 16px;
        }
        .btn-yes:hover {
            background-color: #3aa89b;
        }
        .btn-no {
            background-color: #9b2226;
            padding: 12px 25px;
            font-size: 14px;
        }
        .btn-no:hover {
            background-color: #ae2012;
        }
        
        #finalSection {
            text-align: center;
            padding: 30px 20px;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 85%;
            max-width: 500px;
            box-sizing: border-box;
            background-color: #fff5f7;
            border: 2px solid #ffb3c6;
            border-radius: 20px;
            box-shadow: 0 4px 10px rgba(255, 179, 198, 0.3);
        }
        .final-text {
            color: #ff4d6d;
            font-size: 22px; 
            font-weight: bold;
            margin-bottom: 20px;
        }
        .final-gif img {
            max-width: 200px;
            max-height: 200px;
            border-radius: 15px;
        }
    </style>
</head>
<body>

    <div class="card" id="mainCard">
        <div class="ribbon">🎀</div>
        <div class="title">💕</div>
        
        <div class="verse-container">
            <p class="verse">¿Me perdonas..? 🥺</p>
        </div>

        <div class="gif-box">
            <img id="currentGif" src="" alt="GIF">
        </div>
        
        <div class="btn-container">
            <button class="btn btn-yes" id="btnYes" onclick="handleYesClick()">Sí 💕</button>
            <button class="btn btn-no" id="btnNo" onclick="handleNoClick()">No 🥺</button>
        </div>
    </div>

    <div id="finalSection" style="display: none;">
        <p class="final-text">¡Sabía que dirías que sí!.</p>
        <div class="final-gif">
            <img id="yesGif" src="" alt="GIF Final">
        </div>
    </div>

    <script>
        // Los 5 GIFs para la secuencia cuando presione "No"
        const gifsNo = [
            "https://i.ibb.co/N23wzL7q/triste1-ezgif-com-remove-background.gif",
            "https://i.ibb.co/qLJMjmNF/triste2-ezgif-com-remove-background.gif",
            "https://i.ibb.co/SXm5xZPn/triste3-ezgif-com-remove-background.gif",
            "https://i.ibb.co/RTc1Q3kr/triste4-ezgif-com-remove-background.gif",
            "https://i.ibb.co/3mcQ1dTV/triste5-ezgif-com-remove-background.gif"
        ];

        // GIF para cuando presione "Sí"
        const gifSi = "https://i.ibb.co/6M1c6KP/beso-ezgif-com-remove-background.gif";

        let yesScale = 1.0;
        let noScale = 1.0;
        let gifIndex = 0;

        window.onload = function() {
            document.getElementById('currentGif').src = gifsNo[0];
            document.getElementById('yesGif').src = gifSi;
        };

        function handleNoClick() {
            const btnYes = document.getElementById('btnYes');
            const btnNo = document.getElementById('btnNo');
            const gif = document.getElementById('currentGif');

            // El botón "Sí" se hace cada vez más grande
            yesScale += 0.35;
            btnYes.style.transform = "scale(" + yesScale + ")";

            // El botón "No" se encoge un poquito
            noScale -= 0.08;
            if (noScale > 0.3) {
                btnNo.style.transform = "scale(" + noScale + ")";
            }

            // Cambiar al siguiente GIF triste de ImgBB
            if (gifIndex < gifsNo.length - 1) {
                gifIndex++;
            }
            gif.src = gifsNo[gifIndex];
        }

        function handleYesClick() {
            document.getElementById('mainCard').style.display = 'none';
            document.body.style.backgroundColor = '#ffffff'; 
            document.getElementById('finalSection').style.display = 'block';
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
