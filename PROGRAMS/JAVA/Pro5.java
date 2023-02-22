class Pro5 {
    public static void main(String[] args) {
        int n=153,temp=n,r,sum=0;
        while(n>0) {
            r=n%10;
            sum+=Math.pow(r,3);
            n=n/10;
        }
        if(sum==temp) {
            System.out.print("Armstrong");
        } else {
            System.out.print("Not Armstrong");
        }
    }
}