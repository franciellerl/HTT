from flask import Flask, request, flash, url_for, redirect, render_template
from models import db, migrate, inquilino, proprietario, imovel, aluguel
from sqlalchemy.sql import func

app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:senha123@localhost:5432/crud_htt"
#postgresql://{seu_usuario}:{sua_senha}@{maquina_do_postgres}:{porta}/{banco_postegres}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "random string"
db.init_app(app)
migrate.init_app(app, db)

@app.route('/')
def menu():
    return render_template('menu.html')

#inquilino

@app.route('/inquilino/show_all')
def inquilino_show_all():
   return render_template('inquilino_show_all.html', inquilino = inquilino.query.all())

@app.route('/inquilino/new', methods = ['GET', 'POST'])
def inquilino_new():
    if request.method == 'POST':
        if not request.form['nome'] or not request.form['data_nascimento']:
            flash('Por favor cadastre tudo', 'error')
        else:
            inquilinos = inquilino(request.form['nome'], request.form['data_nascimento'])

            db.session.add(inquilinos)
            db.session.commit()
            flash('Adicionado corretamente')
            return redirect(url_for('inquilino_show_all'))
    return render_template('inquilino_new.html')

@app.route('/inquilino/update/<id>', methods = ['GET', 'POST'])
def inquilino_update(id):
    inquilinos = inquilino.query.filter_by(id=id).first()
    if request.method == 'POST':
            inquilinos.nome = request.form.get('nome')
            inquilinos.data_nascimento = request.form.get('data_nascimento')
            db.session.commit()
            flash('Update Completo', 'success')
            return redirect(url_for('inquilino_show_all'))
    return render_template('inquilino_update.html', inquilinos = inquilinos)

@app.route('/inquilino/delete', methods = ['POST'])
def inquilino_delete():
    inquilinos = inquilino.query.filter_by(id=request.form['id']).first()
    db.session.delete(inquilinos)
    db.session.commit()
    return redirect(url_for('inquilino_show_all'))

#proprietario

@app.route('/proprietario/show_all')
def proprietario_show_all():
   return render_template('proprietario_show_all.html', proprietario = proprietario.query.all())

@app.route('/proprietario/new', methods = ['GET', 'POST'])
def proprietario_new():
    if request.method == 'POST':
        if not request.form['nome'] or not request.form['data_nascimento']:
            flash('Por favor cadastre tudo', 'error')
        else:
            proprietarios = proprietario(request.form['nome'], request.form['data_nascimento'])

            db.session.add(proprietarios)
            db.session.commit()
            flash('Adicionado corretamente')
            return redirect(url_for('proprietario_show_all'))
    return render_template('proprietario_new.html')

@app.route('/proprietario/update/<id>', methods = ['GET', 'POST'])
def proprietario_update(id):
    proprietarios = proprietario.query.filter_by(id=id).first()
    if request.method == 'POST':
            proprietarios.nome = request.form.get('nome')
            proprietarios.data_nascimento = request.form.get('data_nascimento')
            db.session.commit()
            flash('Update Completo', 'success')
            return redirect(url_for('proprietario_show_all'))
    return render_template('proprietario_update.html', proprietarios = proprietarios)

@app.route('/proprietario/delete', methods = ['POST'])
def proprietario_delete():
    proprietarios = proprietario.query.filter_by(id=request.form['id']).first()
    db.session.delete(proprietarios)
    db.session.commit()
    return redirect(url_for('proprietario_show_all'))

#imovel

@app.route('/imovel/show_all')
def imovel_show_all():
   return render_template('imovel_show_all.html', imovel = imovel.query.all())

@app.route('/imovel/new', methods = ['GET', 'POST'])
def imovel_new():
    if request.method == 'POST':
        if not request.form['lougradouro'] or not request.form['cep'] or not request.form['bairro'] or not request.form['cidade']:
            flash('Por favor cadastre tudo', 'error')
        else:
            imoveis = imovel(request.form['lougradouro'], request.form['cep'], request.form['bairro'], request.form['cidade'])
            db.session.add(imoveis)
            db.session.commit()
            flash('Adicionado corretamente')
            return redirect(url_for('imovel_show_all'))
    return render_template('imovel_new.html')

@app.route('/imovel/update/<id>', methods = ['GET', 'POST'])
def imovel_update(id):
    imoveis = imovel.query.filter_by(id=id).first()
    if request.method == 'POST':
            imoveis.lougradouro = request.form.get('lougradouro')
            imoveis.cep = request.form.get('cep')
            imoveis.bairro = request.form.get('bairro')
            imoveis.cidade = request.form.get('cidade')
            db.session.commit()
            flash('Update Completo', 'success')
            return redirect(url_for('imovel_show_all'))
    return render_template('imovel_update.html', imoveis = imoveis)

@app.route('/imovel/delete', methods = ['POST'])
def imovel_delete():
    imoveis = imoveis.query.filter_by(id=request.form['id']).first()
    db.session.delete(imoveis)
    db.session.commit()
    return redirect(url_for('imovel_show_all'))

#aluguel

@app.route('/aluguel/show_all')
def aluguel_show_all():
   return render_template('aluguel_show_all.html', aluguel = aluguel.query.all())

@app.route('/aluguel/new', methods = ['GET', 'POST'])
def aluguel_new():
    if request.method == 'POST':
        if not request.form['num_contrato']:
            flash('Por favor cadastre tudo', 'error')
        else:
            #imovelId = db.session.query(imovel.id).order_by(func.random()).limit(1)
            #propId = db.session.query(proprietario.id).order_by(func.random()).limit(1)
            #idImovel=imovelId, idProp=propId
            #seria necessário um admin pra essa parte funcionar sem interferir no delete/update dos outros
            alugueis = aluguel(request.form['num_contrato'])
            db.session.add(alugueis)
            db.session.commit()
            return redirect(url_for('aluguel_show_all'))
    return render_template('aluguel_new.html')

@app.route('/aluguel/update/<id>', methods = ['GET', 'POST'])
def aluguel_update(id):
    alugueis = aluguel.query.filter_by(id=id).first()
    if request.method == 'POST':
            alugueis.num_contrato = request.form.get('num_contrato')
            db.session.commit()
            return redirect(url_for('aluguel_show_all'))
    return render_template('aluguel_update.html', alugueis = alugueis)

@app.route('/aluguel/delete', methods = ['POST'])
def aluguel_delete():
    alugueis = aluguel.query.filter_by(id=request.form['id']).first()
    db.session.delete(alugueis)
    db.session.commit()
    return redirect(url_for('aluguel_show_all'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)