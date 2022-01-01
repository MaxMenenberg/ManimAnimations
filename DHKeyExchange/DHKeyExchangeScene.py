from manim import *


class DHKeyExchange(Scene):
    def construct(self):
        
        nameFontSize = 25;
        AliceLabel = Text("Alice", font_size = nameFontSize);
        BobLabel = Text("Bob", font_size = nameFontSize);
        EveLabel = Text("Eve", font_size = nameFontSize);
        
        AliceLabel.move_to(LEFT*5+UP*3);
        BobLabel.move_to(RIGHT*5+UP*3);
        EveLabel.move_to(DOWN*2);
        
        self.play(Create(AliceLabel))
        self.play(Create(BobLabel))
        self.play(Create(EveLabel))
        
        self.wait(1)
        
        boxHeight = 6;
        boxWidth = 3;
        
        AliceBox = Rectangle(height = boxHeight, width = boxWidth, color = RED)
        AliceBox.move_to(AliceLabel.get_center() + DOWN*2.5)
        
        BobBox = Rectangle(height = boxHeight, width = boxWidth, color = BLUE)
        BobBox.move_to(BobLabel.get_center() + DOWN*2.5);
        
        EveBox = Rectangle(height = boxHeight, width = boxWidth, color = PURPLE)
        EveBox.move_to(EveLabel.get_center() + UP*2.5);
        
        self.play(Create(AliceBox), Create(BobBox), Create(EveBox))
        self.wait(1)
        
        # Distribute the modulus and base publicly
        eqFontSize = 20;
        publicInfo = Text("p  g", font_size = eqFontSize, color = GREEN)
        
        publicInfo.next_to(AliceLabel, DOWN, buff = 0.2)
        
        self.play(Create(publicInfo))
        
        publicInfoCopyEve = publicInfo.copy()
        publicInfoCopyBob = publicInfo.copy()
        
        self.play(publicInfoCopyEve.animate.next_to(EveLabel, UP, buff = 0.2),\
                  publicInfoCopyBob.animate.next_to(BobLabel, DOWN, buff = 0.2),\
                      run_time = 2)
            
        self.wait(1)
        
        # Alice and Bob create their private keys
        alicePrivateKey = Text("a", font_size = eqFontSize, color = ORANGE)
        bobPrivateKey = Text("b", font_size = eqFontSize, color = ORANGE)
        
        alicePrivateKey.next_to(publicInfo, DOWN, buff = 0.2);
        bobPrivateKey.next_to(publicInfoCopyBob, DOWN, buff = 0.2);
        
        self.play(Create(alicePrivateKey), Create(bobPrivateKey))
        
        # Alice creates and sends her public key
        AlicePublicKeyEq = MathTex("A = g^{a}mod(p)", font_size = eqFontSize+3,\
                                   color = GREEN, substrings_to_isolate="a")
        AlicePublicKeyEq.set_color_by_tex("a", ORANGE)
        AlicePublicKeyEq.next_to(alicePrivateKey, DOWN, buff = 0.2)
        
        AlicePubKeyEqCopy1 = AlicePublicKeyEq.copy()
        AlicePubKeyEqCopy2 = AlicePublicKeyEq.copy()
        
        AlicePublicKeyBob = Text("A", font_size = eqFontSize, color = GREEN)
        AlicePublicKeyBob.next_to(bobPrivateKey, DOWN, buff = 0.2);
        
        AlicePublicKeyEve = Text("A", font_size = eqFontSize, color = GREEN)
        AlicePublicKeyEve.next_to(publicInfoCopyEve, UP, buff = 0.2);
        
        self.play(Create(AlicePublicKeyEq),run_time = 2)
        self.play(Transform(AlicePubKeyEqCopy1, AlicePublicKeyBob),\
                  Transform(AlicePubKeyEqCopy2, AlicePublicKeyEve), run_time = 2)
        self.wait(1)
        
        # Bob creates and sends his public key
        BobPublicKeyEq = MathTex("B = g^{b}mod(p)", font_size = eqFontSize+3,\
                                   color = GREEN, substrings_to_isolate="b")
        BobPublicKeyEq.set_color_by_tex("b", ORANGE)
        BobPublicKeyEq.next_to(AlicePublicKeyBob, DOWN, buff = 0.2)
        
        BobPubKeyEqCopy1 = BobPublicKeyEq.copy()
        BobPubKeyEqCopy2 = BobPublicKeyEq.copy()
        
        BobPublicKeyAlice = Text("B", font_size = eqFontSize, color = GREEN)
        BobPublicKeyAlice.next_to(AlicePublicKeyEq, DOWN, buff = 0.2);
        
        BobPublicKeyEve= Text("B", font_size = eqFontSize, color = GREEN)
        BobPublicKeyEve.next_to(AlicePublicKeyEve, UP, buff = 0.2);
          
        self.play(Create(BobPublicKeyEq), run_time = 2)
        self.play(Transform(BobPubKeyEqCopy1, BobPublicKeyAlice),\
                  Transform(BobPubKeyEqCopy2, BobPublicKeyEve), run_time = 2)
        self.wait(1)
        
        # Alice and Bob compute their shared secret key
        ShrdScrtKeyAlice = MathTex("s = B^{{a}}mod(p)", font_size = eqFontSize+3,\
                                   color = GREEN, substrings_to_isolate= "a" and "s")
        ShrdScrtKeyAlice.set_color_by_tex("s", ORANGE)
        ShrdScrtKeyAlice.set_color_by_tex("a", ORANGE)
        
        ShrdScrtKeyAlice.next_to(BobPublicKeyAlice, DOWN, buff = 0.2)
        
        ShrdScrtKeyBob = MathTex("s = A^{{b}}mod(p)", font_size = eqFontSize+3,\
                                   color = GREEN, substrings_to_isolate="b" and "s")
        ShrdScrtKeyBob.set_color_by_tex("b", ORANGE)
        ShrdScrtKeyBob.set_color_by_tex("s", ORANGE)
        ShrdScrtKeyBob.next_to(BobPublicKeyEq, DOWN, buff = 0.2)
        
        # Copy for transform
        ShrdScrtKeyAliceCopy = ShrdScrtKeyAlice.copy()
        ShrdScrtKeyBobCopy = ShrdScrtKeyBob.copy();
        
        # Expansions of shared secret key
        # ALICE
        ShrdScrtKeyAlice2 = MathTex("s = (g^{{b}})^{{a}}mod(p)",\
                           font_size = eqFontSize+3,\
                           color = GREEN, substrings_to_isolate="a" and "b" and "s")
        ShrdScrtKeyAlice2.set_color_by_tex("a", ORANGE)
        ShrdScrtKeyAlice2.set_color_by_tex("b", ORANGE)
        ShrdScrtKeyAlice2.set_color_by_tex("s", ORANGE)
        ShrdScrtKeyAlice2.next_to(ShrdScrtKeyAlice, DOWN, buff = 0.2)
        
        ShrdScrtKeyAlice2Copy = ShrdScrtKeyAlice2.copy();
        
        ShrdScrtKeyAlice3 = MathTex("s", " = g","^{ba}","mod(p)",\
                           font_size = eqFontSize+3,\
                           color = GREEN)
        ShrdScrtKeyAlice3[0].set_color(ORANGE)
        ShrdScrtKeyAlice3[2].set_color(ORANGE)
        ShrdScrtKeyAlice3.next_to(ShrdScrtKeyAlice2, DOWN, buff = 0.2)
        
        # BOB
        ShrdScrtKeyBob2 = MathTex("s = (g^{{a}})^{{b}}mod(p)",\
                           font_size = eqFontSize+3,\
                           color = GREEN, substrings_to_isolate="a" and "b" and "s")
        ShrdScrtKeyBob2.set_color_by_tex("a", ORANGE)
        ShrdScrtKeyBob2.set_color_by_tex("b", ORANGE)
        ShrdScrtKeyBob2.set_color_by_tex("s", ORANGE)
        ShrdScrtKeyBob2.next_to(ShrdScrtKeyBob, DOWN, buff = 0.2)
        
        ShrdScrtKeyBob2Copy = ShrdScrtKeyBob2.copy();
        
        ShrdScrtKeyBob3 = MathTex("s", " = g","^{ab}","mod(p)",\
                           font_size = eqFontSize+3,\
                           color = GREEN)
        ShrdScrtKeyBob3[0].set_color(ORANGE)
        ShrdScrtKeyBob3[2].set_color(ORANGE)
        ShrdScrtKeyBob3.next_to(ShrdScrtKeyBob2, DOWN, buff = 0.2)
        
        self.play(Create(ShrdScrtKeyAlice), Create(ShrdScrtKeyBob), run_time = 2)
        self.wait(1)
        self.play(Transform(ShrdScrtKeyAliceCopy, ShrdScrtKeyAlice2),\
                  Transform(ShrdScrtKeyBobCopy, ShrdScrtKeyBob2),run_time = 2)
        self.wait(1)
        self.play(Transform(ShrdScrtKeyAlice2Copy, ShrdScrtKeyAlice3),\
                  Transform(ShrdScrtKeyBob2Copy, ShrdScrtKeyBob3),run_time = 2)
        self.wait(1)
        