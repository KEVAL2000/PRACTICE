class Pro2 {
    public static void main(String[] args) {
        int n=8;
        int flag=0;
        if(n==0 || n==1) {
            flag=1;
        } else {
            for(int i=2;i<=n/2;i++) {
                if(n%i==0) {
                    flag=1;
                }
            }
        }
        if(flag==0) {
            System.out.print("Prime");
        } else {
            System.out.print("Not Prime");
        }
    }
}