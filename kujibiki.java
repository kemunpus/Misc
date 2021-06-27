// Build : javac -encoding utf-8 -source 1.5 -target 1.5 kujibiki.java

import java.io.*;
import java.util.Random;

public class kujibiki {

  private static final String [] members = {
    "Aさん",
    "Bさん",
    "Cさん",
    "Dさん"
  };

  public static void main(String [] args) throws Exception {

    Random random = new Random( System.currentTimeMillis() );

    while ( true ) {
      System.out.print( "シャッフルしています\r\n");

      for ( int i = 0; i < members.length * 10 ; i++ ){
        int rh = random.nextInt( members.length );
        int lh = random.nextInt( members.length );

        if ( rh != lh ){
          String tmp = members[ rh ];

          System.out.print( tmp + "さん...          \r");

          members[ rh ] = members[ lh ];
          members[ lh ] = tmp;

          Thread.sleep(100L);
        }
      }

      System.out.print( "シャッフル終わりました！\r\n\r\n");

      BufferedReader in = new BufferedReader( new InputStreamReader( System.in ) );

      for ( int i = 0; i < members.length; i++ ){
        in.readLine();

        System.out.println( members[ i ] + "さん、お願いします！!!\r\n" );
      }
    }
  }
}
