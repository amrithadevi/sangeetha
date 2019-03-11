void main()
{
char a[200];
int n,i,k,t=0;
scanf("%[^\n]s",&a);
for(i=0;a[i]!='\0';i++)
{
t=1;
}
for(n=0;n<i;n++)
{
if(n%2!=0)
{
t=a[n];
a[n]=a[n-1];
a[n-1]=t;
}
}
for(k=0;k<i;k++)
{
printf("%c",a[k]);
}
}
