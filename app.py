from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        previsao_tempo = request.form['previsao_tempo']
        dinheiro_disponivel = float(request.form['dinheiro_disponivel'])
        companhia = request.form['companhia']
        distancia = float(request.form['distancia'])
        dias_de_folga = int(request.form['dias_de_folga'])
        atividades_culturais = request.form.get('atividades_culturais') == 'sim'
        promocao_hoteis = request.form.get('promocao_hoteis') == 'sim'
        trafego_previsto = request.form['trafego_previsto']
        tempo_livre = request.form.get('tempo_livre') == 'sim'
        saude_ok = request.form.get('saude_ok') == 'sim'
        acomodacao_disponivel = request.form.get('acomodacao_disponivel') == 'sim'

        # Verifica as condições para decidir se você deve viajar no final de semana
        if previsao_tempo == "ensolarado":
            if dinheiro_disponivel > 300:
                if companhia == "amigos" or companhia == "família":
                    if distancia >= 300:
                        conclusao = "NÃO, a distância da viagem é muito longa."
                    else:
                        if dias_de_folga >= 2:
                            if atividades_culturais or promocao_hoteis:
                                if trafego_previsto == "baixo":
                                    if tempo_livre:
                                        if saude_ok:
                                            if acomodacao_disponivel:
                                                conclusao = "SIM, você deve viajar no final de semana!"
                                            else:
                                                conclusao = "NÃO, não há acomodação disponível na cidade de destino."
                                        else:
                                            conclusao = "NÃO, você não está com boa saúde."
                                    else:
                                        conclusao = "NÃO, você não tem tempo livre."
                                else:
                                    conclusao = "NÃO, o tráfego está intenso."
                            else:
                                conclusao = "NÃO, não há atividades culturais nem promoção em hotéis."
                        else:
                            conclusao = "NÃO, você não tem dias de folga suficientes."
                else:
                    conclusao = "NÃO, você não tem companhia adequada."
            else:
                conclusao = "NÃO, peça dinheiro a um agiota IMEDIATAMENTE!"
        else:
            conclusao = "NÃO, as condições climáticas não são favoráveis ou você não tem dinheiro suficiente."

        return render_template('resultado.html', conclusao=conclusao)

    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)
