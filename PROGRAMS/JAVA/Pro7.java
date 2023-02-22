// class Pro7 {
//     public static void main(String[] args) {
//         for(int i=0;i<5;i++) {
//             for(int j=0;j<=i;j++) {
//                 System.out.print("*");
//             }
//             System.out.println("");
//         }
//     }
// }

// class Pro7 {
//     public static void main(String[] args) {
//         for(int i=0;i<5;i++) {
//             for(int j=2*(5-i);j>=0;j--) {
//                 System.out.print(" ");
//             }
//             for(int j=0;j<=i;j++) {
//                 System.out.print("* ");
//             }
//             System.out.println("");
//         }
//     }
// }

class Pro7 {
    public static void main(String[] args) {
        int row=10, space=(row-1);
        for(int i=1;i<=row;i++) {
            for(int j=1;j<=space;j++) {
                System.out.print(" ");
            }
            space--;
            for(int j=1;j<=2*i-1;j++) {
                System.out.print("*");
            }
            System.out.println("");
        }

        space=1;
        for(int i=1;i<=row-1;i++) {
            for(int j=1;j<=space;j++) {
                System.out.print(" ");
            }
            space++;
            for(int j=1;j<=2*(row-i)-1;j++) {
                System.out.print("*");
            }
            System.out.println("");
        }
    }
}