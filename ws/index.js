const soap = require('soap');

var url = "https://www3.bcb.gov.br/sgspub/JSP/sgsgeral/FachadaWSSGS.wsdl";

soap.createClient(url, function(err, client){
    //O comando abaixo descreve as funções disponíveis no serviço e como utiliza-los.
    console.log("Descrição do WSDL", client.describe().FachadaWSSGSService.FachadaWSSGS)

    //O comando abaixo usa um dos serviços disponíveis ("getUltimoValorV0")
    client.getUltimoValorVO({in0: 1.0}, function (err, result) {
        if(err){
            console.log(err);
        }else{
            console.log("Resultado", result)
        }
    })
})