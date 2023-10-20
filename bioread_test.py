import sys
import bioread

EXAMPLE_ACQ = "examples/7h.acq"


def print_as_table(lines):
    # Convert all values to strings
    lines = [[str(val) for val in line] for line in lines]
    # Get the maximum width of each column
    widths = [max(map(len, col)) for col in zip(*lines)]
    # Print the table
    for line in lines:
        print("  ".join((val.ljust(width) for val, width in zip(line, widths))))


def main(args):
    if len(args) != 1:
        print("Usage: python main.py [acq_file]")
        return

    data = bioread.read_file(args[0])
    assert data is not None

    lines = []
    for channel in data.channels:
        name = str(channel.name)
        data = channel.data
        if "DI_synchronization_" in name:
            name = "> " + name

        line = [name, len(data), data.min(), data.max(), data.sum(), data.mean()]  # type: ignore
        lines.append(line)

    print_as_table(lines)


if __name__ == "__main__":
    main(sys.argv[1:])

"""Examples:

python bioread_test.py examples/7h.acq

Output on Mac:
TSD115                      51387171  -0.03662109375         0.030517578125       -76605.6396484375    -0.0014907541738080406 
SpO2, OXY100E               51387171  125.44656101661391     125.5006428006329    6447771653.388314    125.4743455985992      
SKT100C_room                51387171  23.01269521660155      23.344150026110828   1191848045.9407477   23.193494071521233     
SKT100C_sub                 51387171  29.594488971118135     29.72842724138181    1524068096.2418365   29.658532792977386     
RSP100C                     51387171  -0.09613037109375      0.01373291015625     -1369612.0825195312  -0.026652801776527672  
EDA100C                     51387171  -0.004578707756053291  0.01373183911894671  248566.91066513592   0.00483713942270019    
PPG100C                     51387171  0.040283203125         0.1287841796875      4387299.780883789    0.0853773363177317     
PPG100C                     51387171  -0.672607421875        -0.6341552734375     -33551446.154785156  -0.6529148326687444    
Rate, OXY100E               51387171  508.248756045387       508.497546968006     26123345506.30136    508.36317699414434     
EGG100C                     51387171  0.011138916015625      0.023956298828125    959572.4333190918    0.018673385100711065   
EMG100C                     51387171  -0.04486083984375      0.048065185546875    90746.98333740234    0.0017659462774746316  
EMG100C                     51387171  -1.07818603515625      1.0882568359375      144419.16244506836   0.0028104127865896406  
EMG100C                     51387171  -0.6146240234375       0.621795654296875    120961.93649291992   0.002353932589379554   
ECG100C_lead_1              51387171  -0.014190673828125     0.013275146484375    -20395.555572509766  -0.00039689975485340036
ECG100C_lead_2              51387171  -0.02105712890625      0.020599365234375    55009.0348815918     0.0010704818695232668  
> DI_synchronization_1      51387171  0.0                    5.0                  64017665.0           1.2457908025331847     
> DI_synchronization_2      51387171  0.0                    5.0                  63964270.0           1.2447517299599933     
ECG100C_lead_3_calculation  51387171  -0.021514892578125     0.02593994140625     75404.59045410156    0.0014673816243766671 

python bioread_test.py examples/11h.acq

Output on Mac:

"""
