#include<stdio.h>
#include<conio.h>
int main(){
	/*input 5
	format *****
	        ***
			 *
	*/
int n,i,j,k,l,temp;;
printf("Enter num");
scanf("%d",&n);
if(n%2==0){
temp=n/2;}
else{
temp=(n/2)+1;}
for(i=1;i<=temp;i++){
for(j=1;j<i;j++){
printf(" ");
}
for(l=i;l<=temp;l++){
printf("*");}
for(k=i+1;k<=temp;k++){
printf("*");}printf("\n");}

return 0;
}

