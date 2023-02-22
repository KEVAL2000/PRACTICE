class Pro3 {
    public static void main(String[] args) {
        int n=342,temp,sum=0;
        temp=n;
        while(n>0) {
            int r=n%10;
            sum=(sum*10)+r;
            n=n/10;
        }
        if(temp==sum) {
            System.out.print("Palindrome");
        } else {
            System.out.print("Not Palindrome");
        }
    }
}