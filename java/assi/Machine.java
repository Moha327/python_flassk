
public class Machine {
    public class MoneySlot{
        public float a;
        public float b;
        public float c;
        public float d;
        public char cardslot;
        public char coinslot;
        public char machine;
        public void n(){
            System.out.println("all cards accepted"); 
        }
        public void nnnnn(){
            System.out.println("there are four demonations:"); 
        }
        public void aaa(){
            System.out.println(.1); 
        }
        public void bbb(){
            System.out.println(.2);
        }
        public void ccc(){
            System.out.println(.5);
        }
        public void ddd(){
            System.out.println(1);
        }
        
    }
     public class SnackSlot{
        
    }
     public class Keypad{
        
    }
    
      
    public static void main(String[] args) {
        Machine myOuter = new Machine();
        MoneySlot o = myOuter.new MoneySlot();
        o.n();
        MoneySlot oo = myOuter.new MoneySlot();
        oo.nnnnn();
        MoneySlot oooo = myOuter.new MoneySlot();
        oooo.aaa();
        MoneySlot eeee = myOuter.new MoneySlot();
        eeee.bbb();
        MoneySlot dddd = myOuter.new MoneySlot();
        dddd.ccc();
        MoneySlot ffff = myOuter.new MoneySlot();
        ffff.ddd();
        
      }
}

