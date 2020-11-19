namespace rockpaperscissors
{
    partial class GameWindow
    {
        private System.ComponentModel.IContainer components = null;
     
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.playerBox = new System.Windows.Forms.PictureBox();
            this.aiBox = new System.Windows.Forms.PictureBox();
            this.rockButton = new System.Windows.Forms.Button();
            this.paperButton = new System.Windows.Forms.Button();
            this.scissorsButton = new System.Windows.Forms.Button();
            this.labelPlayer = new System.Windows.Forms.Label();
            this.labelAI = new System.Windows.Forms.Label();
            this.labelWinLose = new System.Windows.Forms.Label();
            this.labelTimer = new System.Windows.Forms.Label();
            this.labelRound = new System.Windows.Forms.Label();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.restartButton = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.playerBox)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.aiBox)).BeginInit();
            this.SuspendLayout();
            // 
            // playerBox
            // 
            this.playerBox.Location = new System.Drawing.Point(100, 100);
            this.playerBox.Name = "playerBox";
            this.playerBox.Size = new System.Drawing.Size(200, 200);
            this.playerBox.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.playerBox.TabIndex = 0;
            this.playerBox.TabStop = false;
            // 
            // aiBox
            // 
            this.aiBox.Location = new System.Drawing.Point(500, 100);
            this.aiBox.Name = "aiBox";
            this.aiBox.Size = new System.Drawing.Size(200, 200);
            this.aiBox.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.aiBox.TabIndex = 1;
            this.aiBox.TabStop = false;
            // 
            // rockButton
            // 
            this.rockButton.Location = new System.Drawing.Point(200, 400);
            this.rockButton.Name = "rockButton";
            this.rockButton.Size = new System.Drawing.Size(100, 50);
            this.rockButton.TabIndex = 2;
            this.rockButton.Text = "Rock";
            this.rockButton.UseVisualStyleBackColor = true;
            this.rockButton.Click += new System.EventHandler(this.rockButton_Click);
            // 
            // paperButton
            // 
            this.paperButton.Location = new System.Drawing.Point(350, 400);
            this.paperButton.Name = "paperButton";
            this.paperButton.Size = new System.Drawing.Size(100, 50);
            this.paperButton.TabIndex = 3;
            this.paperButton.Text = "Paper";
            this.paperButton.UseVisualStyleBackColor = true;
            this.paperButton.Click += new System.EventHandler(this.paperButton_Click);
            // 
            // scissorsButton
            // 
            this.scissorsButton.Location = new System.Drawing.Point(500, 400);
            this.scissorsButton.Name = "scissorsButton";
            this.scissorsButton.Size = new System.Drawing.Size(100, 50);
            this.scissorsButton.TabIndex = 4;
            this.scissorsButton.Text = "Scissors";
            this.scissorsButton.UseVisualStyleBackColor = true;
            this.scissorsButton.Click += new System.EventHandler(this.scissorsButton_Click);
            // 
            // labelPlayer
            // 
            this.labelPlayer.AutoSize = true;
            this.labelPlayer.Font = new System.Drawing.Font("Showcard Gothic", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.labelPlayer.Location = new System.Drawing.Point(100, 50);
            this.labelPlayer.Name = "labelPlayer";
            this.labelPlayer.Size = new System.Drawing.Size(116, 33);
            this.labelPlayer.TabIndex = 5;
            this.labelPlayer.Text = "Player";
            // 
            // labelAI
            // 
            this.labelAI.AutoSize = true;
            this.labelAI.Font = new System.Drawing.Font("Showcard Gothic", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.labelAI.Location = new System.Drawing.Point(650, 50);
            this.labelAI.Name = "labelAI";
            this.labelAI.Size = new System.Drawing.Size(43, 33);
            this.labelAI.TabIndex = 6;
            this.labelAI.Text = "AI";
            // 
            // labelWinLose
            // 
            this.labelWinLose.AutoSize = true;
            this.labelWinLose.Font = new System.Drawing.Font("Showcard Gothic", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.labelWinLose.Location = new System.Drawing.Point(320, 100);
            this.labelWinLose.Name = "labelWinLose";
            this.labelWinLose.Size = new System.Drawing.Size(121, 27);
            this.labelWinLose.TabIndex = 7;
            this.labelWinLose.Text = "Win / Lose";
            // 
            // labelTimer
            // 
            this.labelTimer.AutoSize = true;
            this.labelTimer.Font = new System.Drawing.Font("Showcard Gothic", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.labelTimer.Location = new System.Drawing.Point(395, 150);
            this.labelTimer.Name = "labelTimer";
            this.labelTimer.Size = new System.Drawing.Size(20, 23);
            this.labelTimer.TabIndex = 8;
            this.labelTimer.Text = "5";
            // 
            // labelRound
            // 
            this.labelRound.AutoSize = true;
            this.labelRound.Font = new System.Drawing.Font("Showcard Gothic", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.labelRound.Location = new System.Drawing.Point(325, 25);
            this.labelRound.Name = "labelRound";
            this.labelRound.Size = new System.Drawing.Size(137, 33);
            this.labelRound.TabIndex = 9;
            this.labelRound.Text = "Rounds: ";
            // 
            // timer1
            // 
            this.timer1.Interval = 1000;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // restartButton
            // 
            this.restartButton.Location = new System.Drawing.Point(299, 481);
            this.restartButton.Name = "restartButton";
            this.restartButton.Size = new System.Drawing.Size(203, 49);
            this.restartButton.TabIndex = 10;
            this.restartButton.Text = "Restart";
            this.restartButton.UseVisualStyleBackColor = true;
            this.restartButton.Click += new System.EventHandler(this.restartButton_Click);
            // 
            // GameWindow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(784, 561);
            this.Controls.Add(this.restartButton);
            this.Controls.Add(this.labelRound);
            this.Controls.Add(this.labelTimer);
            this.Controls.Add(this.labelWinLose);
            this.Controls.Add(this.labelAI);
            this.Controls.Add(this.labelPlayer);
            this.Controls.Add(this.scissorsButton);
            this.Controls.Add(this.paperButton);
            this.Controls.Add(this.rockButton);
            this.Controls.Add(this.aiBox);
            this.Controls.Add(this.playerBox);
            this.Name = "GameWindow";
            this.Text = "Rock Paper Scissors !";
            ((System.ComponentModel.ISupportInitialize)(this.playerBox)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.aiBox)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox playerBox;
        private System.Windows.Forms.PictureBox aiBox;
        private System.Windows.Forms.Button rockButton;
        private System.Windows.Forms.Button paperButton;
        private System.Windows.Forms.Button scissorsButton;
        private System.Windows.Forms.Label labelPlayer;
        private System.Windows.Forms.Label labelAI;
        private System.Windows.Forms.Label labelWinLose;
        private System.Windows.Forms.Label labelTimer;
        private System.Windows.Forms.Label labelRound;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Button restartButton;
    }
}

