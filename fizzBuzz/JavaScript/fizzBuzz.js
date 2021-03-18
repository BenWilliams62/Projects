// FizzBuzz game for numbers between 1 and 100
// It woll not ask for or verify any inputs

const fizz = 3;
const buzz = 5;

for (var i = 1; i <= 100; i++)
{
    let output = "";
    if (i % fizz == 0)
    {
        output += "fizz"
    };
    if (i % buzz == 0)
    {
        output+= "buzz"
    };
    if (output == "")
    {
        output += i
    };
    console.log(output);
}