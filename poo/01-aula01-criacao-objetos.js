//Exemplo 1
var pessoa = {
    nome: 'Luis',
    anoDeNascimento: 1987,
    saldar: function(n){
        console.log(`Oi, ${n}`);
    },
    getIdade: function(){
        return new Date().getFullYear() - this.anoDeNascimento;
    }

}

//Exemplo 2 - Fábrica de objeto
function criaEmpregado(nome, salarioBase, valorHora){
    return {
        nome,
        salarioBase,
        valorHora,
        calculaSalario:()=>{
            return salarioBase + valorHora*100;
        }
    }
}

console.log(criaEmpregado("Luis", 1000, 150))
console.log(criaEmpregado("Luis", 2000, 100).calculaSalario())

//Função construtora de objetos.
function Pessoa2(nome, idade, apelido){

    this.nome = nome,
    this.idade = idade,
    this.apelido = apelido
}

var p = new Pessoa2("Luis", 35, "Tutty");
console.log(p);

//Exemplo 3 - Criação do objeto por meio de Classes
class Pessoa{
    constructor(nome, anoDeNascimento){
        this.nome = nome,
        this.anoDeNascimento = anoDeNascimento
    }

    saldar(n){
        console.log(`Oi, ${n}`);
    }

    getIdade(){
        return new Date().getFullYear() - this.anoDeNascimento;
    }
}
