import string 
import unicodedata
import math

DEBUGGING = True

#dictionary with all the percentage of frequency of letters for each language
english = {'a' : 8.127, 'b' : 1.492, 'c' : 2.782, 'd' : 4.253, 'e' : 12.702, 'f' : 2.228, 'g' : 2.015, 'h'
   : 6.094, 'i' : 6.966, 'j' : 0.153, 'k' : 0.747, 'l' : 4.025, 'm' : 2.406, 'n' : 6.749, 'o' : 7.507, 'p' : 1.929, 'q' :
   0.095, 'r' : 5.987, 's' : 6.327, 't' : 9.056, 'u' : 2.758, 'v' : 1.037, 'w' : 2.365, 'x' : 0.150, 'y' : 1.974, 'z' :
   0.074} 
french = {'a' : 8.000, 'b' : 0.901, 'c' : 3.260, 'd' : 3.669, 'e' : 14.715, 'f' : 1.066, 'g' : 0.866, 'h' :
   0.737, 'i' : 7.529, 'j' : 0.545, 'k' : 0.049, 'l' : 5.456, 'm' : 2.968, 'n' : 7.095, 'o' : 5.378, 'p' : 3.021, 'q' :
   1.362, 'r' : 6.553, 's' : 7.948, 't' : 7.244, 'u' : 6.311, 'v' : 1.628, 'w' : 0.114, 'x' : 0.387, 'y' : 0.308, 'z' :
   0.074}
german = {'a' : 6.51, 'b' : 1.89, 'c' : 3.06, 'd' : 5.08, 'e' : 17.40, 'f' : 1.66, 'g' : 3.01, 'h' :
   4.76, 'i' : 7.55, 'j' : 0.27, 'k' : 1.21, 'l' : 3.44, 'm' : 2.53, 'n' : 9.78, 'o' : 2.51, 'p' : 0.79, 'q' :
   0.02, 'r' : 7.00, 's' : 7.217, 't' : 6.15, 'u' : 4.35, 'v' : 0.67, 'w' : 1.89, 'x' : 0.03, 'y' : 0.04, 'z' :
   1.13}
spanish = {'a' : 12.53, 'b' : 1.42, 'c' : 4.68, 'd' : 5.86, 'e' : 13.68, 'f' : 0.69, 'g' : 1.01, 'h' :
   0.7, 'i' : 6.25, 'j' : 0.44, 'k' : 0.01, 'l' : 4.97, 'm' : 3.15, 'n' : 6.71, 'o' : 8.68, 'p' : 2.51, 'q' :
   0.88, 'r' : 6.87, 's' : 7.98, 't' : 4.63, 'u' : 3.93, 'v' : 0.90, 'w' : 0.02, 'x' : 0.22, 'y' : 0.90, 'z' :
   0.52}

def frequency():
   'Determines the frequency of the letters in a string'
   text = open(raw_input('input path to file \n'), 'r')
   data = text.read()
   data = unicode(data,'utf8',errors='ignore') #converts to unicode encoding to support the accented characters
   if DEBUGGING:  
      print data #debugging stream of the string so far
      print '\n'
   data = unicodedata.normalize('NFKD', data).encode('ascii','ignore').translate(None, string.punctuation).translate(None, '0123456789 \n\t').lower() 
   #normalizes all special characters to their closest ascii equivalent, removes the punctuation, removes spaces and newline characters, convert everything to lower case
   freq = dict() #starts the dictionary for frequency

   for char in data:
      freq[char] = data.count(char) #fills the freq dictionary with the number of times each char occurs
   length = len(data) #gets the length to calculate for percentage later
   total = 0;

   if DEBUGGING:
      print data

   for x in sorted(freq, key=freq.get, reverse = True): #sorts the list by frequency
      print x, "%2.1f%%" % ((float(freq[x]) / length) * 100.0)
      freq[x] = (float(freq[x]) / length) * 100.0
   return freq

def language(freq): #determines what language the text is from
   eng_dist = 0
   fren_dist = 0
   ger_dist = 0
   span_dist = 0
   for char in freq: #compares the frequency for each characters to 4 different dictionaries
      eng_dist += abs(english[char] - freq[char])
      fren_dist += abs(french[char] - freq[char])
      ger_dist += abs(german[char] - freq[char])
      span_dist += abs(spanish[char] - freq[char])
   lang = [eng_dist, fren_dist, ger_dist, span_dist] #finds the minimum distance of all

   print '\nenglish      french        german        spanish'
   print "%2.2f         %2.2f         %2.2f         %2.2f" % (lang[0], lang[1], lang[2], lang[3])

   if span_dist == min(lang): #whichever one is equal to the minimum is the closest language to the input language
      print '\nSpanish'
   elif fren_dist == min(lang):
      print '\nFrench'
   elif ger_dist == min(lang):
      print '\nGerman'
   else:
      print '\nEnglish'

def main():
   language(frequency())

main()