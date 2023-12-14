import java.math.RoundingMode;
import java.text.DecimalFormat;
import java.util.Arrays;

public class JavaBasics {
    /*
     * Arnas Pilipčiuk
     * Prif 21/2
     * 20212598
     */

    /**
     * Javabasics klase skirta Javabasics 1 labaratoriniui darbui atlikti :)
     * 
     * @param args
     */
    public static void main(String[] args) {

        String vardas = "Arnas";
        String pavarde = "Pilipčiuk";
        int n = vardas.length();
        int m = pavarde.length();
        int[][] masyvas = new int[n][m];
        int a = 0;
        int b = n + m;
        double sum = 0;
        int count = 0;
        char[] simboliai = vardas.toLowerCase().toCharArray();
        double[] eilutes = new double[n];
        double[] stulpeliai = new double[m];

        for (char sim : simboliai) {
            if (sim == 'a' || sim == 'e' || sim == 'i' || sim == 'o' || sim == 'u') {
                a++;
            }
        }

        System.out.println("");

        for (int j = 0; j < masyvas[0].length; j++) {
            System.out.print("\t" + (j + 1) + ":");
        }
        System.out.println("");
        System.out.println("");
        for (int i = 0; i < masyvas.length; i++) {
            System.out.print((i + 1) + ":\t");
            for (int j = 0; j < masyvas[i].length; j++) {
                int sk = (int) (Math.random() * (b - a) + a);
                masyvas[i][j] = sk;
                sum += sk;
                System.out.print(masyvas[i][j] + "\t");
            }
            System.out.println("");
            eilutes[i] = sum / m;
            sum = 0;
        }

        // Stulpeliam skaiciuot
        for (int i = 0; i < masyvas[0].length; i++) {
            sum = 0;
            for (int j = 0; j < masyvas.length; j++) {
                sum += masyvas[j][i];
            }
            stulpeliai[i] = sum / n;
        }

        DecimalFormat df = new DecimalFormat("0.0000");
        df.setRoundingMode(RoundingMode.CEILING);

        for (int i = 0; i < eilutes.length; i++) {
            System.out.print(df.format(eilutes[i]) + "\t");

        }

        System.out.println("\t");

        for (int i = 0; i < stulpeliai.length; i++) {
            System.out.print(df.format(stulpeliai[i]) + "\t");

        }
        System.out.println("\t");

        for (

                int i = 0; i < masyvas.length; i++) {
            for (int j = 0; j < masyvas[i].length; j++) {
                if (masyvas[i][j] > eilutes[i])
                    count++;
            }
            System.out.print("Skaiciu " + (i + 1) + " eiluteje kurie didesni nei vidurkis: " + count + "\n");
            count = 0;
        }

        for (int i = 0; i < masyvas.length; i++) {
            for (int j = 0; j < masyvas[i].length; j++) {
                if (i == (a - 1))
                    continue;
                else if (j == (a - 1))
                    continue;
                else {
                    if (masyvas[i][j] > count)
                        count = masyvas[i][j];
                }
            }
        }

        System.out.print("Didziausias neskaitant a eil ir stul: " + count);
        count = 0;
        int[] rikiuotas = new int[m];
        for (int i = 0; i < masyvas.length; i++) {
            for (int j = 0; j < masyvas[i].length; j++) {
                if (i == (a - 1)) {
                    rikiuotas[count] = masyvas[i][j];
                    count++;
                }
            }
        }
        Arrays.sort(rikiuotas);

        System.out.println("\t");

        for (int i = 0; i < rikiuotas.length; i++) {
            System.out.print(rikiuotas[i] + " ");
        }

        int indeksas = 0;
        double indek = 100;

        for (int i = 0; i < stulpeliai.length; i++) {
            if (stulpeliai[i] <= indek) {
                indeksas = i;
                indek = stulpeliai[i];
            }
        }

        count = 100;
        int e = 0;
        int s = 0;

        for (int i = 0; i < masyvas.length; i++) {
            for (int j = 0; j < masyvas[i].length; j++) {
                if (masyvas[i][j] < count) {
                    count = masyvas[i][j];
                    e = i;
                    s = j;
                }
            }
        }
        System.out.print("\n");
        System.out.print("Maziausios reiksmes indeksai: " + e + " " + s + " " + " Maziausia reiksme: " + masyvas[e][s]);
    }

}
