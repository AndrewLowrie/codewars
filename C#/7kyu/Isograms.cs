using System;
using System.Collections.Generic;

public class Kata
{
  public static bool IsIsogram(string word) 
  {
        word = word.ToLower();
        
        if (string.IsNullOrEmpty(word)) return true;

        List<char> lettersInWord = new List<char>();
        var counter = 0;
        var tempLetter = word[counter];

        foreach (var letter in word)
        {
            if (tempLetter.Equals(word[counter + 1])) return false;

            if (lettersInWord.Contains(letter)) return false;

            lettersInWord.Add(letter);
        }

        return true;
  }
}