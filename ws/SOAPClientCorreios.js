const soap = require('soap');

const url = 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl';

soap.createClient(url, function(err, result){
    //Consulta as opções possíveis no serviço dos correios (webservice)
    console.log(result.describe().AtendeClienteService.AtendeClientePort)

    //Utiliza a consulta "consultaCEP" do webservice
    result.consultaCEP({cep: '04105-003'}, function(err, res){
        if(err){
            console.log(err);
        }else{
            console.log('Retorno:', res)
        }
    })
})

