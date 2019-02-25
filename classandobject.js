class Manusia {
    constructor(a,b,c) {
        this.nama = a;
        this.umur = b;
        this.pekerjaan = c;
        this.berbicara = (apayangdingomong) => {
            console.log(apayangdingomong)
            return apayangdingomong + ' I am Groot'
        }
    }
}

var firsthuman = new Manusia('Adam', 900, 'Jobless')
var secondhuman = new Manusia('Eve', 899, 'Wife of the jobless')

// console.log(firsthuman)
// console.log(firsthuman.nama)
// console.log(firsthuman.pekerjaan)
// console.log(secondhuman)
var test = firsthuman.berbicara('Lo keren banget cuy!')
console.log(test)
console.log(apayangdingomong)