import java.util.Scanner;
public class Cuvinte{
    public static void main(String []args){
        String cuvant, vocale = "aeiou";
        StringBuilder cuvantNou = new StringBuilder();
        Scanner citeste = new Scanner(System.in);
        cuvant = citeste.nextLine();
        for(char litera : cuvant.toCharArray()){
            cuvantNou.append(litera);
            if(vocale.indexOf(litera) != -1){
                cuvantNou.append('p').append(litera);
            }
        }
        System.out.println(cuvantNou.toString());

    }
}