from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados Json com as informações das unidades de responsabilidade ambiental
unidades = [
    {
      "ID": 1,
      "Tag": "AC",
      "Estado": "Acre",
      "Titular": "Jose Antonio",
      "Site": "http://www.imac.ac.gov.br/"
    },

    {
      "ID": 2,
      "Tag": "AL",
      "Estado": "Alagoas",
      "Titular": "Marcela Moraes",
      "Site": "http://www.ima.al.gov.br/"
    },
    {
      "ID": 3,
      "Tag": "AM",
      "Estado": "Amazonas",
      "Titular": "Ricardo Santos",
      "Site": "http://www.ipaam.am.gov.br/"
    },
    {
      "ID": 4,
      "Tag": "AP",
      "Estado": "Amapa",
      "Titular": "Maria de Lurdes",
      "Site": "http://www.imap.ap.gov.br/"
    },
    {
      "ID": 5,
      "Tag": "BA",
      "Estado": "Bahia",
      "Titular": "Celia Rodrigues",
      "Site": "http://www.inema.ba.gov.br/"
    },
    {
      "ID": 6,
      "Tag": "CE",
      "Estado": "Ceara",
      "Titular": "Celso de Melo",
      "Site": "http://www.semace.ce.gov.br/"
    },
    {
      "ID": 7,
      "Tag": "DF",
      "Estado": "Distrito Federal",
      "Titular": "Cicero Rodrigues",
      "Site": "http://www.ibram.df.gov.br/"
    },
    {
      "ID": 8,
      "Tag": "ES",
      "Estado": "Espirito Santo",
      "Titular": "Mercedes Rizzo",
      "Site": "http://www.meioambiente.es.gov.br/"
    },
    {
      "ID": 9,
      "Tag": "GO",
      "Estado": "Goias",
      "Titular": "Helton Santos",
      "Site": "http://www.secima.go.gov.br/"
    },
    {
      "ID": 10,
      "Tag": "MA",
      "Estado": "Maranhao",
      "Titular": "Francisco Paiva",
      "Site": "http://www.sema.ma.gov.br/"
    },
    {
      "ID": 11,
      "Tag": "MG",
      "Estado": "Minas Gerais",
      "Titular": "Alexandre Elton",
      "Site": "http://www.semad.mg.gov.br/"
    },
    {
      "ID": 12,
      "Tag": "MS",
      "Estado": "Mato Grosso do Sul",
      "Titular": "Lea Paiva",
      "Site": "http://www.sema.mt.gov.br/"
    },
    {
      "ID": 13,
      "Tag": "MT",
      "Estado": "Mato Grosso",
      "Titular": "Ana Clara",
      "Site": "http://www.sema.mt.gov.br/"
    },
    {
      "ID": 14,
      "Tag": "PA",
      "Estado": "Para",
      "Titular": "Fernanda Pereira",
      "Site": "http://www.sema.pa.gov.br/"
    },
    {
      "ID": 15,
      "Tag": "PB",
      "Estado": "Paraiba",
      "Titular": "Paulo Rodrigues",
      "Site": "http://www.sudema.pb.gov.br/"
    },
    {
      "ID": 16,
      "Tag": "PE",
      "Estado": "Pernambuco",
      "Titular": "Carlos Santana",
      "Site": "http://www.cprh.pe.gov.br/"
    },
    {
      "ID": 17,
      "Tag": "PI",
      "Estado": "Piaui",
      "Titular": "Sheila Bispo",
      "Site": "http://www.semar.pi.gov.br/"
    },
    {
      "ID": 18,
      "Tag": "PR",
      "Estado": "Parana",
      "Titular": "Vera Carla",
      "Site": "http://www.iap.pr.gov.br/"
    },
    {
      "ID": 19,
      "Tag": "RJ",
      "Estado": "Rio de Janeiro",
      "Titular": "Thomas Milton",
      "Site": "http://www.inea.rj.gov.br/"
    },
    {
      "ID": 20,
      "Tag": "RN",
      "Estado": "Rio Grande do Norte",
      "Titular": "Paulo Pedro",
      "Site": "http://www.idema.rn.gov.br/"
    },
    {
      "ID": 21,
      "Tag": "RO",
      "Estado": "Rondonia",
      "Titular": "Leticia Albuquerque",
      "Site": "http://www.sedam.ro.gov.br/"
    },
    {
      "ID": 22,
      "Tag": "RR",
      "Estado": "Roraima",
      "Titular": "Marcos Batista",
      "Site": "http://www.femarh.rr.gov.br/"
    },
    {
      "ID": 23,
      "Tag": "RS",
      "Estado": "Rio Grande do Sul",
      "Titular": "Luis Porto",
      "Site": "http://www.fepam.rs.gov.br/"
    },
    {
      "ID": 24,
      "Tag": "SC",
      "Estado": "Santa Catarina",
      "Titular": "Antonio Safra",
      "Site": "http://www.fatma.sc.gov.br/"
    },
    {
      "ID": 25,
      "Tag": "SE",
      "Estado": "Sergipe",
      "Titular": "Eduardo Pereira",
      "Site": "http://www.adema.se.gov.br/"
    },
    {
      "ID": 26,
      "Tag": "SP",
      "Estado": "Sao Paulo",
      "Titular": "Evair Santos",
      "Site": "http://www.cetesb.sp.gov.br/"
    },
    {
      "ID": 27,
      "Tag": "TO",
      "Estado": "Tocantins",
      "Titular": "Yolanda Francisca",
      "Site": "http://naturatins.to.gov.br/"
    }
]

# GET para obter todos os dados
@app.route('/api', methods=['GET'])
def home():
    return jsonify(unidades), 200

# GET por meio do ID
@app.route('/api/<int:ID>', methods=['GET'])
def unidade_id (ID):
    unidade_id = [unidade for unidade in unidades if unidade['ID'] == ID]
    return jsonify(unidade_id), 200

# GET por meio das Tags dos Estados. Ex: SP
@app.route('/api/<string:Tag>', methods=['GET'])
def unidade_tag (Tag):
    unidade_tag = [unidade for unidade in unidades if unidade['Tag'] == Tag]
    return jsonify(unidade_tag), 200

# DELETE uma unidade ambiental
@app.route('/api/<int:ID>', methods=['DELETE'])
def delete_unidade(ID):
    index = ID - 1
    del unidades[index]
    return jsonify({'message': 'Unidade Excluída com Sucesso'}), 200

# POST para inserir novos dados
@app.route('/api/add', methods=['POST'])
def insert():
      data = request.get_json(force=True)
      unidades.append(data)
      return jsonify(data), 201

# PUT para atualizar dados através do ID
@app.route('/api/<int:ID>', methods=['PUT'])
def change(ID):
      for unidade in unidades:
            if unidade['ID'] == ID:
                  unidade['Titular'] = request.get_json(force=True).get('Titular')
                  return jsonify(unidade), 200

      return jsonify({'Erro': 'Unidade nã Existe'}), 404

if __name__ == '__main__':
  app.run(host='localhost', debug=True, use_reloader=True)