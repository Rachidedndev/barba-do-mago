from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>A Barba do Mago</title>
            <style>
                * { margin: 0; padding: 0; box-sizing: border-box; }
                
                body { 
                    background-color: #121212; 
                    color: #e0e0e0; 
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    min-height: 100vh;
                }

                header {
                    background-color: #1a1a1a;
                    width: 100%;
                    padding: 25px 20px;
                    text-align: center;
                    border-bottom: 3px solid #ff9800;
                    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
                }

                header h1 { 
                    color: #ff9800; 
                    font-size: 2.5rem; 
                    letter-spacing: 2px;
                    text-transform: uppercase;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
                }

                main {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    width: 100%;
                    max-width: 800px;
                    padding: 40px 20px;
                    text-align: center;
                }

                .image-container {
                    width: 100%;
                    max-width: 700px;
                    height: 350px;
                    background-color: #1e1e1e;
                    border: 2px dashed #444;
                    border-radius: 8px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin-bottom: 30px;
                    color: #666;
                    font-style: italic;
                }

                .btn { 
                    display: inline-block; 
                    padding: 14px 28px; 
                    background-color: #ff9800; 
                    color: #121212; 
                    text-decoration: none; 
                    font-weight: bold; 
                    border-radius: 4px; 
                    transition: background 0.2s, transform 0.2s;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
                }

                .btn:hover { 
                    background-color: #e08600; 
                    transform: translateY(-2px);
                }
            </style>
        </head>
        <body>

            <header>
                <h1>A Barba do Mago 🧙‍♂️</h1>
            </header>

            <main>
                <div class="image-container">
                    <span>[Espaço reservado para a imagem do painel]</span>
                </div>

                <a class="btn" href="/admin">Acessar Painel de Controle</a>
            </main>

        </body>
        </html>
    """)