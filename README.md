# BINARY TO DECIMAL FOR IEEE 754 FLOATING POINT VALUES

## General Description
Convert your **Binary Strings** into **Decimal (base-10) Representations** using this simple toolkit.

You have **4** options to choose from that have the following settings:
| Data Type Name | Sign Bit Count | Exponent Bit Count | Mantissa Bit Count |
| :---: | :---: | :---: | :---: |
| `float` | 1 | **8** | **23** |
| `double` | 1 | **11** | **52** |
| `long double` | 1 | **15** | **112** |
| `custom` | 1 | `q` | `p - 1` |

`p` and `q` are additional user inputs for a custom `p` + `q` bit long representation of a floating point value in binary.

Simply enter the desired values for the prompted questions and the code should return a decimal (base-10) representation for the floating point value your entered in binary. Due to the restriction of representing infinitely many floating points in a finite number of bits, there will be **rounding** and therefore the expected value may not match the outcome due to the `p` + `q` long **fixed-width** binary representation.

### User Input Error Handling
If the user enters a binary stream that is **less** than `exponent bit count` + `mantissa bit count` + `sign bit count` long, then the algorithm effectively pads the left of the binary with `0`s until it has met the size requirement. If the user enters a binary stream that is **greater** than `exponent bit count` + `mantissa bit count` + `sign bit count` long then the algorithm effectively truncates the excess bits so that the size requirement is properly met. *Invalid inputs* are handled using while loops that keep prompting questions for the valid inputs and provide explanation for why the inputs were *invalid*.