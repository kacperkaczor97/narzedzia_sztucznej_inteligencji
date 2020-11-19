using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace rockpaperscissors
{
    /// <summary>
    /// Klasa GameWindow posiada wszystkie potrzebne metody do stowrzenia aplikacji okienkowej RockPaperScisors
    /// </summary>
    public partial class GameWindow : Form
    {
        /// <remarks>
        /// Na początku zostały zadeklarowane wszystkie potrzebne zmienne:
        /// <example>
        /// <code>
        /// int rounds; 
        /// int timePerRound; 
        /// bool gameOver;
        /// string aiChoice;
        /// string playerChoice;
        /// int playerScore;
        /// int aiScore;
        /// </code>
        /// </example>  
        /// </remarks>
        
        int rounds = 1;
        int timePerRound = 6;
        bool gameOver = false;

        string[] aiChocieList = { "Rock", "Paper", "Scissor" };

        int randomNumber = 0;
        Random rnd = new Random();

        string aiChoice;
        string playerChoice;

        int playerScore;
        int aiScore;
  
        public GameWindow()
        {
            InitializeComponent();
            timer1.Enabled = true;
            playerChoice = "none";
            labelTimer.Text = "5";

            // Początkowe boxy mają prezentować znaki zapytani 
            playerBox.Image = Properties.Resources.znakZapytania;
            aiBox.Image = Properties.Resources.znakZapytania;

        }
        /// <summary>
        /// Metoda rockButton_Click zostaje wywołana w momencie ,gdy Player wybierze przycisk "Rock" i ustawia playerChoice na "Rock" + playerBox.Image na obraz Kamienia
        /// </summary>
        private void rockButton_Click(object sender, EventArgs e)
        {
            playerBox.Image = Properties.Resources.Kamien;
            playerChoice = "Rock";
        }
        
        /// <summary>
        /// Metoda paperButton_Click zostaje wywołana w momencie ,gdy Player wybierze przycisk "Paper" i ustawia playerChoice na "Paper" + playerBox.Image na obraz Papieru
        /// </summary>
        private void paperButton_Click(object sender, EventArgs e)
        {
            playerBox.Image = Properties.Resources.Papier;
            playerChoice = "Paper";
        }

        /// <summary>
        /// Metoda scissorsrButton_Click zostaje wywołana w momencie ,gdy Player wybierze przycisk "Scissors" i ustawia playerChoice na "Scissors" + playerBox.Image na obraz Nożyce
        /// </summary>
        private void scissorsButton_Click(object sender, EventArgs e)
        {
            playerBox.Image = Properties.Resources.Nozyce;
            playerChoice = "Scissor";
        }

        /// <summary>
        /// Metoda restartButton_Click zostaje wywołana w momencie ,gdy Player wybierze przycisk "Restart", dzięki tej metodzie rozpoczynamy grę od nowa
        /// </summary>
        private void restartButton_Click(object sender, EventArgs e)
        {
            playerScore = 0;
            aiScore = 0;
            rounds = 1;

            labelWinLose.Text = "Player: " + playerScore + " - " + aiScore + " :AI ";

            playerChoice = "none";

            timer1.Enabled = true;

            playerBox.Image = Properties.Resources.znakZapytania;
            aiBox.Image = Properties.Resources.znakZapytania;
        }

        /// <summary>
        /// Metoda timer1_Tick służy do odlicznia czasu między pojawieniem się wyborów graczy, podczas odliczania Player ma możliwość zmiany decyzji
        /// </summary>
        private void timer1_Tick(object sender, EventArgs e)
        {
            timePerRound -= 1;
            labelTimer.Text = timePerRound.ToString();
            labelRound.Text = "Round: " + rounds;

            if (timePerRound < 1)
            {
                timer1.Enabled = false;
                timePerRound = 6;

                randomNumber = rnd.Next(0, aiChocieList.Length);
                aiChoice = aiChocieList[randomNumber];

                /// <remarks>
                /// Switch przyjmuje losową liczbę z zakresu 0-2 i na jej podstawie wybiera Rock,Paper lub Scissor dla AI
                /// </remarks>
                switch (aiChoice)
                {
                    case "Rock":
                        aiBox.Image = Properties.Resources.Kamien;
                        break;
                    case "Paper":
                        aiBox.Image = Properties.Resources.Papier;
                        break;
                    case "Scissor":
                        aiBox.Image = Properties.Resources.Nozyce;
                        break;
                }

                /// <remarks>
                /// Gra toczy się na przestrzeni 3 rund 
                /// </remarks>
                if (rounds < 3)
                {
                    checkGame();
                }
                else
                {
                    checkDecision();
                }
                
            }
        }

        /// <summary>
        /// Metoda checkGame sprawdza status danej rundy i jest odpowiedzialna za przydzielanie punktów
        /// </summary>
        private void checkGame()
        {
            // AI Wins
            if (playerChoice == "Rock" && aiChoice == "Paper")
            {
                aiScore++;
                rounds++;
                MessageBox.Show("AIWins Paper over Rock");
                startNextRoud();
            }
            else if (playerChoice == "Scissor" && aiChoice == "Rock")
            {
                aiScore++;
                rounds++;
                MessageBox.Show("AIWins Rock breaks Scissor");
                startNextRoud();
            }
            else if (playerChoice == "Paper" && aiChoice == "Scissor")
            {
                aiScore++;
                rounds++;
                MessageBox.Show("AIWins Scissor cuts Paper");
                startNextRoud();
            }
            //Player wins
            else if (playerChoice == "Rock" && aiChoice == "Scissor")
            {
                playerScore++;
                rounds++;
                MessageBox.Show("PlayerWins Rock breaks Scissor");
                startNextRoud();
            }
            else if (playerChoice == "Paper" && aiChoice == "Rock")
            {
                playerScore++;
                rounds++;
                MessageBox.Show("PlayerWins Paper over Rock");
                startNextRoud();
            }
            else if (playerChoice == "Scissor" && aiChoice == "Paper")
            {
                playerScore++;
                rounds++;
                MessageBox.Show("PlayerWins Scissor cuts Paper");
                startNextRoud();
            }
            // Make Choice
            else if (playerChoice == "none")
            {
                MessageBox.Show("Make a choice");
                startNextRoud();

            }
            // Draw
            else if (playerChoice == aiChoice)
            {
                MessageBox.Show("Draw");
                startNextRoud();
            }
            else
            {
                MessageBox.Show("Draw");
                startNextRoud();
            }
        }

        /// <summary>
        /// Metoda checkDecision sprawdza czy zostały sprawdzone warunki dla zwycięstwa Playera lub AI
        /// </summary>
        private void checkDecision()
        {
            if (playerScore == 2)
            {
                MessageBox.Show("Player Won !");
            }
            else if (playerScore == aiScore && playerChoice == "Rock" && aiChoice == "Scissor")
            {
                MessageBox.Show("Player Won !");
            }
            else if (playerScore == aiScore && playerChoice == "Scissor" && aiChoice == "Paper")
            {
                MessageBox.Show("Player Won !");
            }
            else if (playerScore == aiScore && playerChoice == "Paper" && aiChoice == "Rock")
            {
                MessageBox.Show("Player Won !");
            }
            else if (aiScore == 2)
            {
                MessageBox.Show("AI Won !");
            }
            else if (playerScore == 1 & aiScore == 1 & playerChoice == aiChoice)
            {
                MessageBox.Show("Overtime!");
                startNextRoud();
            }
            else
            {
                MessageBox.Show("AI Won !");
            }
        }

        /// <summary>
        /// Metoda startNextRoud rozpoczyna nam kolejną rundę
        /// </summary>
        private void startNextRoud()
        {
            if (gameOver == true)
            {
                return;
            }

            // pokazuje nam biezący wynik
            labelWinLose.Text = "Player: " + playerScore + " - " + aiScore + " :AI ";

            playerChoice = "none";

            timer1.Enabled = true;

            // podczas odliczania boxy są ustawione na znak zapytania
            playerBox.Image = Properties.Resources.znakZapytania;
            aiBox.Image = Properties.Resources.znakZapytania;
        }
    }
}

