class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        int[] countArray = new int[26];
        for (int i = 0; i < s.length(); ++i) {
            countArray[s.charAt(i) - 'a'] += 1;
            countArray[t.charAt(i) - 'a'] -= 1;
        }
        for (int c : countArray) {
            if (c != 0) return false;
        }
        return true;
    }
}
