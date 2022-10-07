//Definição da classe Node, contendo nó da lista encadeada.

class Node{
    constructor(item=null, next=null){
        this.item = item;
        this.next = next;       
    }

    getItem(){
        return this.item;
    }


    setItem(item){
        this.item = item;
    }
    
    getNext(){
        return this.next;
    }
    
    setNext(next){
            this.next = next;
        }
    
    print(){
        console.log("Item: " + this.getItem() + "\nNext: " + this.getNext());
    }
}

//Definição da classe lista encadeada, usando Node como nó da lista.
class LinkedList{

    constructor(){
        this.head = null;
        this.tail = null;
    }

    setHead(node){
        this.head = node;
    }

    getHead(){
        return this.head;
    }

    setTail(node){
        this.tail = node;
    }

    getTail(){
        return this.tail;
    }

    insertEnd(node){
        if(this.getHead() === null){
            this.setHead(node);
            this.setTail(node);
        }else{
            let tail = this.getTail();
            tail.setNext(node);
            this.setTail(node);
        }
    }

    print(){
        if(!this.head){
            console.log("Empty list.")
        }else{
            let node = this.getHead();
            do{
                console.log(node.getItem());
                node = node.getNext();
            }while(node != null)
        }
    }
}

//Teste de implementação da classe Node.
let a = new Node();
a.setItem("Node 1");

let b = new Node();
b.setItem("Node 2");

console.log(a);


//Teste de implementação de lista encadeada.
let l = new LinkedList();
l.print();
l.insertEnd(a);
l.insertEnd(b);


c = new Node();
c.setItem('Node 3')
l.insertEnd(c);
d = new Node();
d.setItem('Node 4')
l.insertEnd(d);
l.print();

let e = new Node(item='Node 5')
l.insertEnd(e);
l.print()