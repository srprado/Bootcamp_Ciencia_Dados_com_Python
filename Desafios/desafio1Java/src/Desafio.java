
import java.util.Scanner;

public class Desafio {
    public static float calculoSalario(float salBruto, float valorBeneficios){
        float percentImposto;
        if(salBruto <= 1100)
            percentImposto = 5;
        else if(salBruto > 1100 && salBruto <= 2500)
            percentImposto = 10;
        else
            percentImposto = 15;   
 
        float salarioLiquido = salBruto - ((salBruto*percentImposto)/100) + valorBeneficios;
        
        return salarioLiquido;
    }
    
    public static void main(String[] args){
        Scanner teclado = new Scanner(System.in);
        
        System.out.print("Digite seu salário bruto: ");
        float salBruto = teclado.nextFloat();
        
        System.out.print("Digite o valor total dos benefícios: ");
        float valorBeneficios = teclado.nextFloat();
        
        float valorSalario = calculoSalario(salBruto, valorBeneficios); 
        
        System.out.printf("Valor do salário a ser recebido: %.2f", valorSalario);        
    }
}
