// 0 1 1 2 3
class Pro1 {
	static int i=2,a=0,b=1,c;
	public static void fibbo(int count) {
		if(count>0) {
			c=a+b;
			a=b;
			b=c;
			System.out.print(c+" ");
			fibbo(count-1);
		}
	}
	public static void main(String[] args) {
		System.out.print(a+" "+b+" ");
		fibbo(10);
	}
}


class Pro1 {
	public static void main(String[] args) {
		int a=0,b=1,c,count=10,i;
		System.out.print(a+" "+b+" ");
		for(i=2;i<count;++i)  {
			System.out.print(a+b+" ");
			c=a+b;
			a=b;
			b=c;
		}
	}
}