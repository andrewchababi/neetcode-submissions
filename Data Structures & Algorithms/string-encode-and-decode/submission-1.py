class Solution:

    def encode(self, strs: List[str]) -> str:
        sentence = ""
        for word in strs:
            sentence += word + '='
        
        return sentence

    def decode(self, s: str) -> List[str]:
        result = s.split("=")
        result.pop()
        return result
