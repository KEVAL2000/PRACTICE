class Pro4 {
    public static void main(String[] args) {
        int n=5,fact=1;
        for(int i=1;i<=n;i++) {
            fact=fact*i;
        }
        System.out.print(fact);
    }
}

class Pro4 {
    public static int factorial(int n) {
        if(n==0) {
            return 1;
        } else {
            return n*factorial(n-1);
        }
    }
    public static void main(String[] args) {
        int fact=1;
        fact=factorial(5);
        System.out.print(fact);
    }
}