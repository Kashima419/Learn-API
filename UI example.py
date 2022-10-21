import clr
import sys
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
import System.Drawing
import System.Windows.Forms
from System.Drawing import *
from System.Windows.Forms import *

class Poppup(Form):
	def __init__(self):
		self.out = []
		self.mystyle()
	def mystyle(self):
		self._combo1 = System.Windows.Forms.ComboBox()
		self._buttonOk = System.Windows.Forms.Button()
		self._buttonCancel = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._name = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# combobox
		self._combo1.FormattingEnabled = True
		self._combo1.Items.AddRange(System.Array[System.Object](["Wall","Floor""Rebar"]))
		self._combo1.Location = System.Drawing.Point(200, 50)
		self._combo1.Text = "Category"
		self._combo1.Size = System.Drawing.Size(80, 20)
		self._combo1.TabIndex = 0
		self._combo1.SelectedIndexChanged += self.ComboBox1SelectedIndexChanged
		# name
		self._name.Location = System.Drawing.Point(200, 100)
		self._name.Text = "100"
		self._name.Size = System.Drawing.Size(80, 20)
		self._name.TabIndex = 1
		# buttonOk
		self._buttonOk.Location = System.Drawing.Point(200, 150)
		self._buttonOk.Size = System.Drawing.Size(50, 20)
		self._buttonOk.TabIndex = 2
		self._buttonOk.Text = "OK"
		self._buttonOk.UseVisualStyleBackColor = True

		# buttonCancel
		self._buttonCancel.Location = System.Drawing.Point(40, 150)
		self._buttonCancel.Size = System.Drawing.Size(50, 20)
		self._buttonCancel.TabIndex = 2
		self._buttonCancel.Text = "Cancel"
		self._buttonCancel.UseVisualStyleBackColor = True
		#
		# MainForm
		self.AutoSize = True
		self.ClientSize = System.Drawing.Size(300, 200)
		self.Controls.Add(self._name)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._buttonOk)
		self.Controls.Add(self._buttonCancel)
		self.Controls.Add(self._combo1)
		self.MaximizeBox = False
		self.MinimizeBox = False
		self.Name = "MainForm"
		self.ShowIcon = False
		self.Text = "My_UI"
		self.ResumeLayout(True)
		self.PerformLayout()

	def buttonOk1Click(self, sender, e):
		self.out.append(self._input.Text)
		self.out.append(self._name.Text)
		self.out.append(self._combo1.SelectedItem)
		self.Close()  
		
	def ComboBox1SelectedIndexChanged(self, sender, e):
		pass

	def Label1Click(self, sender, e):
		pass

form = Poppup()
Application.Run(form)