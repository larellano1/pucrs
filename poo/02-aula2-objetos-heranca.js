//Objeto pai
class Pessoa{
    #nome; //Quando eu incluo o #, eu torno essa variável privada em JS, impedindo a utilização fora da classe.
    #anoDeNascimento; 
    constructor(nome, anoDeNascimento){
        this.#nome = nome, //São das variáveis privadas definidas acima.
        this.#anoDeNascimento = anoDeNascimento
    }

    saldar(n){
        console.log(`Oi, ${n}`);
    }

    getIdade(){
        return new Date().getFullYear() - this.anoDeNascimento;
    }
}

//Objeto filho
class Funcionario extends Pessoa{
    constructor(salarioBase, nome, anoDeNascimento){
        super(nome,anoDeNascimento)
        this.salarioBase = salarioBase;
    }
}

var f = new Funcionario(3000, "Luis", 1987);
console.log(f);
console.log(f.saldar("Felipe"));

//Polimorfismo
class Terceiro extends Pessoa{
    saldar(n){
        super.saldar(n);
        console.log("Executado pelo filho.")
        return true;
    }
}
var t = new Terceiro("Julio", 2016);
console.log(t.saldar("Amigo"));

//Exemplo de método static.
class ValidadorCPF{
    static validar(cpf){ //ao declarar o método como static, eu permito que ele seja acessado sem criar uma instância do objeto
        if(cpf === ''){
            return false;
        }
        return true;
    }
}

console.log(ValidadorCPF.validar('000')) //Método acessado sem instância criada.