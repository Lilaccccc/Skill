import com.raquo.laminar.api.L.*
import com.raquo.laminar.nodes.ReactiveHtmlElement
import org.scalajs.dom.HTMLDivElement
import scala.scalajs.js
import scala.scalajs.js.annotation.*

object MainApp {
  def appElement(): ReactiveHtmlElement[HTMLDivElement] = {
    div(
      h1("Hello Scala.JS~!")
    )
  }
}
